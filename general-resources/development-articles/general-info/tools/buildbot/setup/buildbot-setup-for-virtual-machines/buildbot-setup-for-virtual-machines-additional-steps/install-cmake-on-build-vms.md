# Install cmake on build VMs

[MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) Requires cmake. Install cmake on all -build VMs (and other Unix-like machines) with:

```
wget http://www.cmake.org/files/v2.8/cmake-2.8.8.tar.gz
tar -zxvf cmake-2.8.8.tar.gz
cd cmake-2.8.8;./configure
make
sudo make install
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
