# Installation

## System Requirements

- **Operating System**: Linux (Debian/Ubuntu/RHEL), macOS 10.15+, or Windows 10/11
- **CPU**: 4+ cores recommended
- **RAM**: Minimum 8GB, 16GB+ recommended
- **Storage**: 10GB for installation, additional space for document storage
- **Database**: MariaDB 10.6+ or compatible MySQL 8.0+
- **Python**: Version 3.9+ (included in the installation package)

## Installation Procedure

### Linux (Debian/Ubuntu)

1. Download the installation package:
   ```bash
   wget https://downloads.mariadb.com/databridge/mariadb-databridge-1.0.0.deb
   ```

2. Install the package:
   ```bash
   sudo dpkg -i mariadb-databridge-1.0.0.deb
   ```

3. Install dependencies:
   ```bash
   sudo apt-get install -f
   ```

### Linux (RHEL/CentOS)

1. Download the installation package:
   ```bash
   wget https://downloads.mariadb.com/databridge/mariadb-databridge-1.0.0.rpm
   ```

2. Install the package:
   ```bash
   sudo rpm -i mariadb-databridge-1.0.0.rpm
   ```

### Windows

1. Download the installation package from the MariaDB website.
2. Run the `.msi` installer.
3. Follow the installation wizard instructions.
