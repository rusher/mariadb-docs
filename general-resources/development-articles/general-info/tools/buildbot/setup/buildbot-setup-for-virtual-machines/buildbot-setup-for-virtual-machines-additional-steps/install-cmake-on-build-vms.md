# Install cmake on build VMs

[MariaDB 5.5](broken-reference) Requires cmake. Install cmake on all -build VMs (and other Unix-like machines) with:

```
wget http://www.cmake.org/files/v2.8/cmake-2.8.8.tar.gz
tar -zxvf cmake-2.8.8.tar.gz
cd cmake-2.8.8;./configure
make
sudo make install
```

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
