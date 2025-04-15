
# Galera Test Repositories

To facilitate development and QA, we have created some test repositories for
the Galera wsrep provider.


These are **test** repositories. There will be periods when they do not work at
all, or work incorrectly, or possibly cause earthquakes, typhoons, and
tornadoes. You have been warned.


## Galera Test Repositories for YUM


Replace `<code class="fixed" style="white-space:pre-wrap"><span class="si">${</span><span class="nv">dist</span><span class="si">}</span>
</code>` in the code below for
the YUM-based distribution you are testing. Valid distributions are:


* `<code>centos5-amd64</code>`
* `<code>centos5-x86</code>`
* `<code>centos6-amd64</code>`
* `<code>centos6-x86</code>`
* `<code>centos7-amd64</code>`
* `<code>rhel5-amd64</code>`
* `<code>rhel5-x86</code>`
* `<code>rhel6-amd64</code>`
* `<code>rhel6-x86</code>`
* `<code>rhel6-ppc64</code>`
* `<code>rhel7-amd64</code>`
* `<code>rhel7-ppc64</code>`
* `<code>rhel7-ppc64le</code>`
* `<code>fedora22-amd64</code>`
* `<code>fedora22-x86</code>`
* `<code>fedora23-amd64</code>`
* `<code>fedora23-x86</code>`
* `<code>fedora24-amd64</code>`
* `<code>fedora24-x86</code>`
* `<code>opensuse13-amd64</code>`
* `<code>opensuse13-x86</code>`
* `<code>sles11-amd64</code>`
* `<code>sles11-x86</code>`
* `<code>sles12-amd64</code>`
* `<code>sles12-ppc64le</code>`


```
# Place this code block in a file at /etc/yum.repos.d/galera.repo
[galera-test]
name = galera-test
baseurl = http://yum.mariadb.org/galera/repo/rpm/${dist}
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1
```

## Galera Test Repositories for APT


Replace `<code class="fixed" style="white-space:pre-wrap"><span class="si">${</span><span class="nv">dist</span><span class="si">}</span>
</code>` in the code below
for the APT-based distribution
you are testing. Valid ones are:


* `<code>wheezy</code>`
* `<code>jessie</code>`
* `<code>sid</code>`
* `<code>precise</code>`
* `<code>trusty</code>`
* `<code>xenial</code>`


```
# run the following command:
sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xcbcb082a1bb943db 0xF1656F24C74CD1D8

# Add the following line to your /etc/apt/sources.list file:
deb http://yum.mariadb.org/galera/repo/deb ${dist} main
```
