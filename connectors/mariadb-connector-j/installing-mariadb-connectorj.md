# Installing MariaDB Connector/J

{% hint style="info" %}
The most recent [_**Stable**_](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-release-criteria) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-connectors/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/java/mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes)
{% endhint %}

[Download MariaDB Connector/J](https://mariadb.com/downloads/connectors/)

## Installing MariaDB Connector/J with a Package Manager

The recommended way to install MariaDB Connector/J is to use a package manager like [Maven](https://maven.apache.org/what-is-maven.html) or [Gradle](https://gradle.org/).

### Installing MariaDB Connector/J with Maven

To install MariaDB Connector/J with [Maven](https://maven.apache.org/what-is-maven.html), add the following dependency to your `pom.xml` configuration file:

```xml
<dependency> 
<groupId>org.mariadb.jdbc</groupId>
<artifactId>mariadb-java-client</artifactId>
<version>$VERSION</version>
</dependency>
```

Be sure to replace `$VERSION` with a valid MariaDB Connector/J version number. See [About MariaDB Connector/J: Java Compatibility](https://mariadb.com/kb/en/about-mariadb-connector-j/#java-compatibility) to determine which MariaDB Connector/J release series supports your Java version.

### Installing MariaDB Connector/J with Gradle

To install MariaDB Connector/J with [Gradle](https://gradle.org/), add the following dependency to your `build.gradle` configuration file:

```java
implementation 'org.mariadb.jdbc:mariadb-java-client:$VERSION'
```

Be sure to replace `$VERSION` with a valid MariaDB Connector/J version number. See [About MariaDB Connector/J: Java Compatibility](https://github.com/mariadb-corporation/docs-connectors/blob/test/kb/en/about-mariadb-connector-j/README.md#java-compatibility) to determine which MariaDB Connector/J release series supports your Java version.

[Gradle configuration](java-connector-using-gradle.md).

## Installing MariaDB Connector/J Manually with the JAR File

It is not generally the recommended method, but MariaDB Connector/J can also be installed by manually installing the `.jar` file to a directory in your `[CLASSPATH](https://docs.oracle.com/javase/tutorial/essential/environment/paths.html)`.

MariaDB Connector/J `.jar` files can be downloaded from the following URL:

*

## Installing MariaDB Connector/J from Source

This section deals with building the connector from source and testing it. If\
you have downloaded a ready-built connector, in a jar file, then this section\
may be skipped.

The source code is available at the [mariadb-connector-j repository](https://github.com/MariaDB/mariadb-connector-j) on GitHub. You can clone it by executing the following:

```bash
git clone https://github.com/MariaDB/mariadb-connector-j.git
```

If you would prefer a packages source tarball release, then MariaDB Connector/J `.jar` source code tarballs can be downloaded from the following URL:

*

MariaDB Connector/J has the following build requirements:

* [Maven](https://maven.apache.org/what-is-maven.html)
* Java JDK

If you would like to run the unit tests, then you'll need a MariaDB or MySQL server. It has to meet the following requirements:

* It must be listening on `localhost` on TCP port `3306`.
* It must have a database called `testj`.
* It must have a `root` user account with an empty password.

If you would like to build MariaDB Connector/J and run the unit tests, then execute the following:

```bash
mvn package
```

If you would like to build MariaDB Connector/J without running the unit tests, then execute the following:

```bash
mvn -Dmaven.test.skip=true package
```

Once the build is complete, you should have a `.jar` file with a name like `mariadb-java-client-x.y.z.jar` in the `target` subdirectory.


{% @marketo/form formId="4316" %}
