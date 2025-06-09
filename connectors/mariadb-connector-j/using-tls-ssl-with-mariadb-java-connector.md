# using-tls-ssl-with-mariadb-java-connector

## Using TLS/SSL with MariaDB Connector/J

## Overview

This document explains how to configure the MariaDB Java driver to support TLS/SSL.

Data can be encrypted during transfer using the Transport Layer Security (TLS) protocol.\
TLS/SSL permits transfer encryption, and optionally server and client identity validation.

{% hint style="info" %}
The term SSL (Secure Sockets Layer) is often used interchangeably with TLS, although strictly-speaking the SSL protocol is the predecessor of TLS, and is not implemented as it is now considered insecure.
{% endhint %}

### Server configuration

To ensure that SSL is correctly configured on the server, the query "SELECT @@have\_ssl;" must return YES. If not, please refer to the [server documentation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption).

Connecting to a server that doesn't support TLS with TLS option set, an exception "Trying to connect with ssl, but ssl not enabled in the server" will be thrown.

### TLS Protocol Version Selection

The MariaDB Java driver by default uses java default supported protocols .\
If the servers are MariaDB on Unix or version >= 10.2 , consider adding TLSv1.2 protocol.\
This can be set using the "enabledSslProtocolSuites" option (example: enabledSslProtocolSuites=TLSv1.2,TLSv1.3).

In addition to the protocol, the driver relies on the Java default cipher list.\
The Java default enabled ciphers are [listed here](https://docs.oracle.com/javase/8/docs/technotes/guides/security/SunProviders.html#SupportedCipherSuites).\
JAVA allows cipher suites to be removed/excluded from use in the security policy using the Java system property "jdk.tls.disabledAlgorithms".\
The specific list of ciphers to be used can be set using the "enabledSslCipherSuites" driver option (example : "enabledSSLCipherSuites=TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA256,...")

## One way SSL authentication

By default, the driver can be configured to use TLS, even if the user used for authentication is not set to use TLS, but the recommendation is to use a user created with "REQUIRE SSL". See [CREATE USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user) for more details, to ensure connector use TLS.

Example;

```sql
CREATE USER 'myUser'@'%' IDENTIFIED BY 'MyPwd';
GRANT ALL ON db_name.* TO 'myUser'@'%' REQUIRE SSL;
```

Since version 3 of the connector, TLS is enable client side setting option "sslMode".\
The following values are supported:

* disable: Do not use SSL/TLS (default)
* trust: Only use SSL/TLS for encryption. Do not perform certificate or hostname verification.
* verify-ca: Use SSL/TLS for encryption and perform certificates verification, but do not perform hostname verification.
* verify-full: Use SSL/TLS for encryption, certificate verification, and hostname verification. This is the standard TLS behavior. Alias "true"/"1" are possible like "sslMode=true"

{% hint style="info" %}
Before connector 3 version, other options where used in order to use TLS:

* useSsl: boolean, indicate if TLS has to be enable.
* trustServerCertificate: boolean, when enable with useSsl=true, corresponds to sslMode=trust
* disableSslHostnameVerification: boolean, when enable with useSsl=true and trustServerCertificate is not enable, corresponds to sslMode=verify-ca
{% endhint %}

To ensure TLS is enable server side, first try with option "sslMode=trust".

```java
try (Connection con = DriverManager.getConnection("jdbc:mariadb://localhost/myDb?user=myUser&password=MyPwd"
		+ "&sslMode=trust")) {
	try (Statement stmt = con.createStatement()) {
		stmt.execute("select 1");
	}
}
```

Please note that this is not safe for production use, since even if all exchanges will be encrypted, the identity of the server is not verified, permitting man in the middle fake servers.

To validate the server identity, server root certificates and intermediate certificates must be trusted client side.

There are several ways to achieve this:

* Java has a default truststore that contains well-known CAs including Let's Encrypt (since java 8u101), VeriSign, Entrust, and GTE CyberTrust.trusted Certificate Authorities (CA). If the server certificate is signed using a certificate chain using a root CA known in java default truststore, nothing has to be configured client side. The location of default truststore is set in system property "javax.net.ssl.trustStore".
* provide the certificate using option "serverSslCert".
* Zero-configuration TLS encyption using 3.4+ version of the connector and [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/what-is-mariadb-114)+ server. See dedicated chapter.

By default when sslMode is set (not disabled), connector will use "serverSslCert" is set or the default truststore if not. Using default truststore can be disable setting option "fallbackToSystemTrustStore" to false.

### Java default truststore

Java trustStore is a file that contains certificates of trusted SSL servers, or of Certificate Authorities trusted to identify servers. Truststore can be protected by a password.

The Java search order for locating the trust store is:

1. system property "javax.net.ssl.trustStore"
2. $JAVA\_HOME/lib/security/jssecacerts
3. $JAVA\_HOME/lib/security/cacerts (shipped by default)

To add a certificate from a CA not included in the truststore, locate the default truststore on your system. The default truststore is located in the $JAVA\_HOME/jre/lib/security/cacerts.

```java
//copy the java truststore to jssecacerts
cp $JAVA_HOME/jre/lib/security/cacerts $JAVA_HOME/jre/lib/security/jssecacerts
//add your certificat to truststore
keytool -importcert -file myCA-root.cer -alias myCA -keystore /usr/java/default/jre/lib/security/jssecacerts -storepass changeit
```

with our previous example, change sslMode to "verify-full":

```java
try (Connection con = DriverManager.getConnection("jdbc:mariadb://localhost/myDb?user=myUser&password=MyPwd"
		+ "&sslMode=verify-full")) {
	try (Statement stmt = con.createStatement()) {
		stmt.execute("select 1");
	}
}
```

### Provide certificate directly

The "serverSslCert" option permits setting the certificate location.\
The location can be used in one of 3 forms:

* serverSslCert=/path/to/cert.pem (full path to certificate)
* serverSslCert=classpath:relative/cert.pem (relative to current classpath)
* or as verbatim DER-encoded certificate string "------BEGING CERTIFICATE-----..." .

Example :

```java
try (Connection con = DriverManager.getConnection("jdbc:mariadb://localhost/myDb?user=myUser&password=MyPwd&serverSslCert=/path/to/cert.pem&&sslMode=verify-full")) {
	try (Statement stmt = con.createStatement()) {
		stmt.execute("select 1");
	}
}
```

### Zero-configuration TLS encryption

TLS use has been simplified with MariaDB Server 11.4. For MariaDB Connector/J 3.4+ to establish an SSL encrypted connection to MariaDB Server 11.4, enabling SSL does not require any special configuration apart from using "sslMode=verify-full"

During TLS exchange, server will send certificate, client will validate server identity with the certificate fingerprint and password hashing. This required that the password is not empty.

## Mutual (2-way) authentication

Mutual SSL authentication or certificate based mutual authentication refers to two parties authenticating each other through verifying the provided digital certificate so that both parties are assured of the others' identity.

To enable mutual authentication, the user must be created with "REQUIRE X509" so the server asks the driver for client certificates. See [CREATE USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user) for more details.

Example:

```sql
CREATE USER 'myUser'@'%' IDENTIFIED BY 'MyPwd';
GRANT ALL ON db_name.* TO 'myUser'@'%' REQUIRE X509;
```

**If the user is not set with REQUIRE X509, only one way authentication will be done**

The client (driver) must then have its own certificate too (and related private key).\
If the driver doesn't provide a certificate, and the user used to connect is defined with "REQUIRE X509", the server will then return a basic "Access denied for user".

Java stores this client certificate and private key in a keyStore file.\
A keystore file is similar to trustore, in fact trustore and keystore are often the same file.

Example of generating a keystore in JKS format :

```bash
# generate a keystore with the client cert & key
  openssl pkcs12 \
    -export \
    -in "${clientCertFile}" \
    -inkey "${clientKeyFile}" \
    -out "${tmpKeystoreFile}" \
    -name "mariadbAlias" \
    -passout pass:kspass

  # convert PKSC12 to JKS
  keytool \
    -importkeystore \
    -deststorepass kspass \
    -destkeypass kspass \
    -destkeystore "${clientKeystoreFile}" \
    -srckeystore ${tmpKeystoreFile} \
    -srcstoretype PKCS12 \
    -srcstorepass kspass \
    -alias "mariadbAlias"
```

Like truststore, the Java default keystore can be used, then no additional option is needed, or a dedicated keystore by using the "keyStore" option to indicate location and the "keyStorePassword" option to indicate the keystore password.\
In JKS keystore, an additional password for a specific key may have been set. The "keyPassword" option permits setting this password.

## Troubleshooting

### SSL not enabled on server

If the following error occurs: "java.sql.SQLException: Trying to connect with ssl, but ssl not enabled in the server", SSL is not enabled on the server-side.\
Since the "useSSL=true" option is set, the connection failed.\
Execute "show variables like '%ssl%';" on the server-side to identify the SSL issue.

### Server certificate is not provided to client

When the driver tries to connect using SSL, but no certificate is provided, or the "trustServerCertificate=true" option is not set, the driver will fail with the following exception "Caused by: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target"

Solution:

* not recommended: set the "sslMode" option to "trust" value
* add the server certificate to the driver (see documentation above).

### java.sql.SQLInvalidAuthorizationSpecException: Could not connect: Access denied for user

This can occur for a number of reasons:

* The user / password is incorrect.
* Some SSL options have been set on the user (can be checked using "select SSL\_TYPE, SSL\_CIPHER, X509\_ISSUER, X509\_SUBJECT FROM mysql.user u where u.User = '';) and the connection attempt doesn't meet those requirements.


{% @marketo/form formid="4316" %}
