
# Uploading Package to PPA


After creating a Launchpad account:


#### Docker build, cloning the MariaDB repository and mapping it to the docker container


1. mkdir mariadb-source


2. cd mariadb-source


3. vi Dockerfile


4. Copy the following contents to Dockerfile:


```
# MariaDB 10.3 Ubuntu 17.10 build environment
# Published as mariadb-10-3-ubuntu-17.10-build-env
FROM ubuntu:17.10
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
apt-get install -y --no-install-recommends \
systemd \
devscripts \
build-essential \
lsb-release \
equivs \
git \
curl \
git-buildpackage \
nano \
vim \
pristine-tar

RUN curl -skO https://raw.githubusercontent.com/ottok/mariadb-10.1/ubuntu-17.10/debian/control

ENV GIT_SSL_NO_VERIFY true

RUN mk-build-deps -t 'apt-get -y -o Debug::pkgProblemResolver=yes --no-install-recommends' -i control

ENV container docker
ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
```

5. Run `<code>docker build . -t ubuntu-17.10-packaging</code>`


6. Do git clone of the latest repository:


`<code class="fixed" style="white-space:pre-wrap">cd && mkdir debian-packaging && cd debian-packaging && git clone https://salsa.debian.org/mariadb-team/mariadb-10.1.git</code>`


#### Generate, publish and upload PGP key


7. Generate OpenPGP key with the following command:


`<code class="fixed" style="white-space:pre-wrap">$ gpg --gen-key </code>`


* select (1) RSA and RSA
* Keysize: accept 2048
* Valid for: accept 0
* Type name, email and comment (comment is optional)
* Type 0
* Type passphrase (twice)
* Follow instructions to help generate a random key
* Keep the Key ID and fingerprint text, they are needed in the next step


Set generated key as default in `<code>~/.bashrc</code>`


`<code class="fixed" style="white-space:pre-wrap">$ nano ~/.bashrc </code>`


[.. add this ..]


`<code class="fixed" style="white-space:pre-wrap">export GPGKEY=<key_id></code>`


Restart GPG-agent and source '/.bashrc', or restart session


8. Publish the key to the key server:


`<code class="fixed" style="white-space:pre-wrap">gpg --keyserver keyserver.ubuntu.com --send-keys 12345678</code>` and substitute `<code>12345678</code>` with your key's id


* If this gives timeout error, keep re-trying after a while


9. Upload the key's fingerprint here:
Upload [ImportingYourPGPKey](https://help.launchpad.net/YourAccount/ImportingYourPGPKey) fingerprint here
[+editpgpkeys](https://launchpad.net/~rsurve/+editpgpkeys)


10. `<code>gpg --export [your-key-id] > ~/debian-packaging/pub.key</code>`


11. `<code>gpg --export-secret-key [your-key-id] > ~/debian-packaging/secret.key</code>`


`<code class="fixed" style="white-space:pre-wrap">gpg -k</code>`


^Should show the key


12. How to upload:
[How-to-upload-to-Launchpad-PPA-repository-(.deb-packages)](https://github.com/exelearning/iteexe/wiki/How-to-upload-to-Launchpad-PPA-repository-(.deb-packages))


13. Open `<code>/etc/devscripts.conf</code>`


And look for this line:


`<code class="fixed" style="white-space:pre-wrap">DEBSIGN_MAINT</code>`


Uncomment it and add your name there


`<code class="fixed" style="white-space:pre-wrap">export DEBEMAIL=[your-email-id]</code>`


#### From inside the container


14. `<code>docker run -v ~/debian-packaging/:/repo -it ubuntu-17.10-packaging bash</code>`


15. `<code>apt-get install devscripts</code>`


16. `<code>gpg --import pub.key</code>`


17. `<code>gpg --import secret.key</code>`


18. `<code>gpg -k</code>`


19. `<code>cd /repo/mariadb-10.1 && git fetch && git checkout pristine-tar && git checkout ubuntu-17.10</code>`


20. `<code>git clean -dffx && git reset --hard HEAD</code>`


21. `<code>export DEB_BUILD_OPTIONS="parallel=10 nocheck"</code>` or `<code>export DEB_BUILD_OPTIONS="parallel=5 nocheck"</code>`


22. Go to `<code>/repo</code>` folder (Inside docker) and delete all the files except mariadb-10.1 folder:


`<code class="fixed" style="white-space:pre-wrap">rm *</code>`


23.
`<code class="fixed" style="white-space:pre-wrap">gbp buildpackage </code>`


#### For re-running the set up container


24. To generate an ID, run:
`<code class="fixed" style="white-space:pre-wrap">docker commit <container-id></code>` This will generate an ID.


For restarting the same container again use this ID:
`<code class="fixed" style="white-space:pre-wrap">docker run -v ~/debian-packaging/:/repo -it <ID> bash</code>`


25. Last command for uploading package to PPA:


`<code class="fixed" style="white-space:pre-wrap">backportpackage -u <your-ppa-address> -d <ubuntu-version-to-backport-to> -S ~<a-version-suffix-name-for-this-package> <the-most-recent-dsc-file></code>`


Example:


`<code class="fixed" style="white-space:pre-wrap">backportpackage -u ppa:cvicentiu/mariadb-10.0-dev2 -d bionic -S ~testtry mariadb-10.1_10.1.30-0ubuntu0.17.10.1.dsc</code>`


Run this command in the `<code>/repo</code>` folder, where the `<code>.dsc</code>` file is located
It should ask for the gpg key password again


* Docker tutorial available here:
[edit#slide=id.p4](https://docs.google.com/presentation/d/1euJrK7MJ9QRvwW33iwESIEo5Dyi7JWExIKFrISktFao/edit#slide=id.p4)

