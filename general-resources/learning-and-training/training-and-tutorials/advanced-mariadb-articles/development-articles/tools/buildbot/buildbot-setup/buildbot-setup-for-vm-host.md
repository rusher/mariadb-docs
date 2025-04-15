
# Buildbot Setup for VM host

This page documents the general setup process for a server that is acting as
virtual machine host, like those documented in the
[Buildbot Setup for Virtual Machines](buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-debian/buildbot-setup-for-virtual-machines-debian-4-i386.md)
section.


1. Provision hardware with most recent Ubuntu LTS release


1. Add host to DNS


1. Apply updates (replace `<code><host></code>` with hostname)


```
ssh <host>.mariadb.net
sudo apt-get update
sudo apt-get dist-upgrade
```

1. install some favorite packages (these aren't necessarily required, but I like them)


```
sudo apt-get install tree renameutils vim-nox
```

1. a buildbot admin needs to add the new host to the allowed list of rsync
 clients on the VM master (whichever host is the official host of VM
 files) The VM master changes periodically, so check to make sure you have
 the correct one.


```
vi /etc/rsyncd.conf
```

1. make a `<code>/kvm/</code>` dir and rsync it with the VM master above. The dir often
 resides at `<code>/home/kvm/</code>` (or wherever the storage drive is) and is then
 linked to `<code>/kvm/</code>`. The VMs rely on the `<code>/kvm/vms/</code>` path, so
 the `<code>/kvm/</code>` location is required.


```
vm_master="hostname"      # ask for this from a buildbot admin
mkdir /home/kvm
ln -sv /home/kvm /kvm
rsync --dry-run --delete --exclude=deprecated \\
  --exclude=iso --exclude=lost+found -avPL ${vm_master}::kvm/ /home/kvm/
# assuming the dry-run looks good, start the "real" rsync in a screen session
screen
rsync --delete --exclude=deprecated --exclude=iso --exclude=lost+found -avPL ${vm_master}::kvm/ /home/kvm/
```

1. detatch from screen session with `<code>Ctrl+a d</code>`


1. Configure vim.basic as the default editor (optional)


```
update-alternatives --config editor
```

1. install buildbot-slave, bzr, and kvm


```
sudo apt-get install bzr git buildbot-slave qemu kvm 
sudo apt-get install libsdl2-2.0-0
```

1. add a default user, and then add the user to the appropriate groups


```
username="mydefaultusername"
sudo adduser ${username}
for group in sudo tty kvm;do
  sudo adduser ${username} ${group}
done
```

1. logout then back in as the default user and change the password


1. set up the `<code>/.ssh/authorized_keys</code>` file so you can login that way


1. create other standard users and set up their ssh keys (optional)


1. turn off password login (WARNING: be sure to have your ssh key setup
 before doing this!) and disallow all root logins and password logins (it
 is safer to only allow logins using ssh keys with regular users):


```
sudo perl -i -pe "s/#PasswordAuthentication yes/PasswordAuthentication no/" /etc/ssh/sshd_config
sudo perl -i -pe "s/PermitRootLogin yes/PermitRootLogin no/" /etc/ssh/sshd_config
sudo /etc/init.d/ssh restart
```

1. checkout mariadb-tools


```
mkdir ~/src
cd ~/src/
bzr branch lp:mariadb-tools
```

1. put runvm in the right place


```
sudo cp -v ~/src/mariadb-tools/buildbot/runvm /usr/local/bin/
ls -l /usr/local/bin/
```

1. add the buildbot user to the kvm and tty groups


```
sudo adduser buildbot kvm
sudo adduser buildbot tty
```

1. A buildbot admin will need to add this builder
 to the `<code>maria-master-private.cfg</code>` file on the `<code>${buildmaster}</code>` and
 also add it to the `<code>c['slaves']</code>` array in `<code>maria-master.cfg</code>` then
 create the buildslave using the hostname and whatever `<code>${password}</code>` was
 agreed upon by you and the buildbot admin:


```
sudo buildslave create-slave /var/lib/buildbot/slaves/maria buildbot.askmonty.org ${host} ${password}
```

1. add the following to `<code>/etc/default/buildslave</code>` (replace `<code>${hostname}</code>`
 with the name of the host)


```
HOME=/var/lib/buildbot
SLAVE_ENABLED[1]=1
SLAVE_NAME[1]="${hostname} maria slave"
SLAVE_USER[1]="buildbot"
SLAVE_BASEDIR[1]="$HOME/slaves/maria"
SLAVE_OPTIONS[1]=""
SLAVE_PREFIXCMD[1]=""
```

1. edit the admin and host files and add contact information and details on
 the builder:


```
sudo vi /var/lib/buildbot/slaves/maria/info/*
```

1. copy over the buildbot .ssh dir from terrier:


```
scp terrier.askmonty.org:buildbot-ssh.tar.gz .

cd /var/lib/buildbot
sudo tar -zxvf ~/buildbot-ssh.tar.gz
sudo chown -Rv buildbot: .ssh
sudo chmod -v 700 .ssh
sudo chmod -Rv go-r .ssh
```

1. Edit /etc/passwd and change the buildbot user's shell from `<code>/bin/false</code>`
 to `<code>/bin/bash</code>`


1. su to the buildbot user and copy in the `<code>/etc/skel</code>` files


```
sudo su - buildbot
cp -v /etc/skel/.bash* .
cp -v /etc/skel/.profile .
exit
```

1. change ownership of the `<code>buildbot/slaves</code>` dir to `<code>buildbot:buildbot</code>`


```
sudo chown -Rv buildbot:buildbot ~buildbot/slaves
```

1. move the `<code>/var/lib/buildbot</code>` directory to `<code>/home</code>` (or whatever
 location you want to use to store things) and then link it back


```
sudo mv -vi /var/lib/buildbot /home/;cd /var/lib/;sudo ln -sv /home/buildbot ./
```

1. update `<code>/etc/default/locale</code>` and change it to: `<code>LANG=en_US.UTF-8</code>`


```
sudo vi /etc/default/locale
sudo locale-gen
```

1. monitor the rsync, wait for it to finish


1. once the rsync is finished, test the runvm script


```
sudo su - buildbot
for i in '/kvm/vms/vm-xenial-amd64-serial.qcow2 6666 qemu64' '/kvm/vms/vm-xenial-i386-serial.qcow2 6666 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/testtest/')" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get update" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y patch libaio1 debconf-utils unixodbc libxml2 libjudydebian1" \
    "= scp -P $2 /kvm/vms/my55.seed /kvm/vms/sources.append buildbot@localhost:/tmp/" \
    "sudo debconf-set-selections /tmp/my55.seed" \
    "sudo sh -c 'cat /tmp/sources.append >> /etc/apt/sources.list'"; \
done
```

1. Remove the "testtest" VMs we created above


```
rm -v /kvm/vms/*testtest*
```

1. Start the buildslave


```
sudo /etc/init.d/buildslave start

tail -f ~buildbot/slaves/maria/twistd.log
```

1. ssh to `<code>${buildmaster}</code>` and add this new host to `<code>kvm_slaves</code>` in
 the `<code>maria-master.cfg</code>` file


```
sudo vi /etc/buildbot/maria-master.cfg
```

1. still on `<code>${buildmaster}</code>`, test and then reload buildbot


```
cd /etc/buildbot
sudo -u buildbot PYTHONPATH=/usr/local/buildbot/lib/python python -c 'exec open("maria-master.cfg", "r")'
sudo /etc/init.d/buildmaster reload
sudo tail -f /var/lib/buildbot/maria/twistd.log
```
