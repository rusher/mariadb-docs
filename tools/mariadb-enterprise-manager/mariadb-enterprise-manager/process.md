---
hidden: true
---

# Process

Created by Stefan Hinz, last modified by Egor Ustinov on Sep 23, 2025

This page is NOT part of the draft documentation, but rather documents internal processes.

## General Notes to Team & Writer

[This sheet](https://docs.google.com/spreadsheets/d/1sfpfnm6qffNzjdywexxN09uCbZ6noP2tstrjpja8xFk/edit?usp=sharing) covers content owners.

Put documentation on GitHub 2 weeks before launch.

## Notes for Customer-Facing Docs

Installation of EM is done in Docker, mostly for simplicity:

* Dependencies
* Updates

Reference page to mirror for EM: https://mariadb.com/docs/tools/mariadb-enterprise-operator/customer-access-to-docker-mariadb-com#customer-credentials

## Installation Instructions for Trying out EM

To use the product before launch, install virtualization software like VirtualBox, Vagrant, or Parallels.

Then create VMs (1 VM for Enterprise Manager, and 1 VM for each database you plan to monitor).

Using multiple VMs is an alternative to using multiple physical computers.

## CentOS9 VM Template for VirtualBox

The VM template works only in VirtualBox, and only on x86-architecture computers.

https://drive.google.com/drive/folders/19moMRXcIPv5FNriiAndf9IgZR\_nkUPVL?usp=drive\_link

## Installation on Linux

{% hint style="info" %}
Sections below marked "Only for internal, not needed for customers" are intended for internal use.
{% endhint %}

### Gcloud CLI installation (Only for internal, not needed for customers)

{% code title="Install Google Cloud CLI (yum)" %}
```bash
sudo tee -a /etc/yum.repos.d/google-cloud-sdk.repo << EOM
[google-cloud-cli]
name=Google Cloud CLI
baseurl=https://packages.cloud.google.com/yum/repos/cloud-sdk-el9-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=0
gpgkey=https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOM
dnf install google-cloud-cli
```
{% endcode %}

### Gcloud authentication (Only for internal, not needed for customers)

{% code title="Gcloud auth commands" %}
```bash
gcloud auth configure-docker us-central1-docker.pkg.dev
gcloud auth login
```
{% endcode %}

### Registry authentication (customers will use registry at docker.mariadb.com)

{% code title="Docker login" %}
```bash
docker login us-central1-docker.pkg.dev
```
{% endcode %}

### Enterprise Manager installation (customers won't need to specify --registry parameter)

{% code title="Run installer" %}
```bash
./install.sh --registry us-central1-docker.pkg.dev/mariadb-es-docker-registry/docker-proxy-dev
```
{% endcode %}

## Installation Script for VM Installation

Save the following script, make it executable, and run it.

{% code title="install.sh" %}
```bash
#!/bin/bash
#
# Copyright (c) 2025 MariaDB plc. All rights reserved, proprietary and confidential.
#
# This is UNPUBLISHED PROPRIETARY SOURCE CODE AND A TRADE SECRET of MariaDB plc, www.mariadb.com

registry="docker.mariadb.com"
tag="latest"
pull_images=1
start_containers=1

#
# Options
#
while :; do
  case $1 in
    --registry) # Which registry to use
      registry=$2
      shift
      ;;
    --tag) # Which tag to use
      tag=$2
      shift
      ;;
    --no-pull) # Don't pull images before starting Enterprise Manager
      pull_images=0
      ;;
    --no-start) # Don't start the Enterprise Manager
      start_containers=0
      ;;
    *) break
  esac
  shift
done

#
# Check dependencies
#
if [[ -d enterprise-manager ]]
then
  echo "Error: Enterprise Manager is already installed at $(pwd)/enterprise-manager/"
  exit 1
fi

if [[ "$(arch)" == "x86_64" ]]
then
  architecture=amd64
else
  echo "Error: Only x86_64 is currently supported, found: $(arch)"
  exit 1
fi

for cmd in curl tar sed openssl
do
  if ! command -v $cmd > /dev/null
  then
    echo "Error: '$cmd' not found in PATH, please install it first."
    exit 1
  fi
done

if ! command -v docker > /dev/null
then
  echo "Error: 'docker' not found in PATH."
  echo "  Docker is required to run MariaDB Enterprise Manager."
  echo "  Please install Docker and ensure it is available in your PATH."
  echo "  Installation instructions: https://docs.docker.com/engine/install/"
  exit 1
fi

if docker compose > /dev/null 2>&1
then
  docker_compose="docker compose"
else
  if docker-compose > /dev/null 2>&1
  then
    docker_compose="docker-compose"
  else
    echo "Error: 'docker-compose' not found in PATH, please install it first."
    exit 1
  fi
fi

#
# Everything seems to be present, try to download the Enterprise Manager as well as any missing tools
#
# Use a temporary directory so that the cleanup is easy
oldpwd=$(pwd)
tmpdir=$(mktemp -d)
cd "$tmpdir" || exit 1

# Logs an error, removes the temporary directory and exits
install_error() {
  echo "Error: $1"
  rm -r "$tmpdir"
  exit 1
}

echo "Downloading Enterprise Manager..."
if command -v oras > /dev/null
then
  oras_cmd="oras"
else
  VERSION="1.2.2"
  oras_release="https://github.com/oras-project/oras/releases/download/v${VERSION}/oras_${VERSION}_linux_${architecture}.tar.gz"
  curl -s -LO "$oras_release" || install_error "Failed to download Oras from: $oras_release"
  tar -zxf "oras_${VERSION}_linux_${architecture}.tar.gz" || install_error "Failed to unpack downloaded Oras tarball"
  oras_cmd="./oras"
fi

$oras_cmd pull "$registry/enterprise-manager:$tag" || install_error "Failed to pull Enterprise Manager"
tar -zxf enterprise-manager.tar.gz || install_error "Failed to unpack Enterprise Manager"
mv enterprise-manager "$oldpwd"/enterprise-manager || install_error "Failed to copy Enterprise manager to $oldpwd"
rm -r "$tmpdir"
cd "$oldpwd"/enterprise-manager || install_error "Failed to change directory to $oldpwd/enterprise-manager/"

#
# Enterprise Manager is downloaded and unpacked, ask questions about the configuration
#
# Logs an error and exits
startup_error() {
  echo "Error: $1"
  exit 1
}

protocol="https"
def_host="localhost"
def_port="8090"

cat <<EOF
Enterprise Manager must be configured with a public facing domain name or IP address from which it is accessed by users.
EOF

# Try to find out if there's an IP address and suggest that as the default.
# This makes it work better with virtual machines.
if command -v hostname > /dev/null && command -v awk > /dev/null
then
  first_ip=$(hostname -I|awk '{print $1}')
  if [[ -n "$first_ip" ]]
  then
    echo "Found IP addresses: $(hostname -I)"
    def_host="$first_ip"
  fi
fi

read -erp "Enter the hostname or IP address (default: $def_host): " user_host
if [ -z "$user_host" ]
then
  user_host=$def_host
fi

read -erp "Enter the port that Enterprise Manager listens on (default: $def_port): " user_port
if [ -z "$user_port" ]
then
  user_port=$def_port
fi

# Configure the public facing hostname
sed -i "s%MEMA_HOSTNAME=https://localhost:8090%MEMA_HOSTNAME=$protocol://$user_host:$user_port%" .env

# Configure nginx
sed -i "s%8090 ssl%$user_port ssl%" nginx/nginx.conf

echo "Generating new TLS certificates..."
if openssl req -nodes -x509 -newkey rsa:2048 -batch \
    -subj "/CN=$user_host/O=MariaDB Enterprise Manager CA" \
    -addext "subjectAltName=DNS:$user_host,IP:$user_host" \
    -keyout certs/ca-key.pem -out certs/ca-cert.pem && \
   openssl req -nodes -newkey rsa:2048 -batch \
    -subj "/CN=$user_host/O=MariaDB Enterprise Manager" \
    -addext "subjectAltName=DNS:$user_host,IP:$user_host" \
    -keyout certs/key.pem.new -out certs/cert.req && \
   openssl x509 -req -days 3000 -copy_extensions copy \
    -in certs/cert.req -out certs/cert.pem.new \
    -CA certs/ca-cert.pem -CAkey certs/ca-key.pem
then
  rm certs/cert.req
  mv certs/cert.pem.new certs/cert.pem
  mv certs/key.pem.new certs/key.pem
  chmod a+r certs/*.pem
else
  startup_error "Failed to generate new TLS certificates"
fi

if [ $pull_images -ne 0 ]
then
  $docker_compose pull
fi

if [ $start_containers -ne 0 ]
then
  $docker_compose up -d || startup_error "Failed to start Enterprise Manager"
fi

cat <<EOF
Enterprise Manager has been installed. Default username set to 'admin' and password to 'mariadb'.
Go to: $protocol://$user_host:$user_port/
EOF
```
{% endcode %}

## Attachments

* &#x20;[install.sh](broken-reference) (text/x-bash)

Document generated by Confluence on Oct 13, 2025 16:28

http://www.atlassian.com/
