# Database Design Example Phase 3: Implementation

This article follows on from [Database Design Example Phase 2: Design](database-design-example-phase-2-design.md).

With the design complete, it's time to [install MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb) and run the [CREATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create) statements, as follows:

```
CREATE DATABASE poets_circle;

CREATE TABLE poet (
  poet_code INT NOT NULL, 
  first_name VARCHAR(30),
  surname VARCHAR(40), 
  address VARCHAR(100), 
  postcode VARCHAR(20),
  email VARCHAR(254), 
  PRIMARY KEY(poet_code)
);

CREATE TABLE poem(
  poem_code INT NOT NULL, 
  title VARCHAR(50),
  contents TEXT, 
  poet_code INT NOT NULL, 
  PRIMARY KEY(poem_code),
  INDEX(poet_code), 
  FOREIGN KEY(poet_code) REFERENCES poet(poet_code) 
);

CREATE TABLE publication(
  publication_code INT NOT NULL,
  title VARCHAR(100),
  price MEDIUMINT UNSIGNED,
  PRIMARY KEY(publication_code)
);

CREATE TABLE poem_publication(
  poem_code INT NOT NULL,
  publication_code INT NOT NULL, 
  PRIMARY KEY(poem_code, publication_code), 
  INDEX(publication_code),
  FOREIGN KEY(poem_code) REFERENCES poem(poem_code),
  FOREIGN KEY(publication_code) REFERENCES publication(publication_code)
);

CREATE TABLE sales_publication(
  sales_code INT NOT NULL,
  publication_code INT NOT NULL,
  PRIMARY KEY(sales_code, publication_code)
); 

CREATE TABLE customer(
  customer_code INT NOT NULL, 
  first_name VARCHAR(30), 
  surname VARCHAR(40), 
  address VARCHAR(100), 
  postcode VARCHAR(20), 
  email VARCHAR(254), 
  PRIMARY KEY(customer_code)
);

CREATE TABLE sale(
  sale_code INT NOT NULL, 
  sale_date DATE,
  amount INT UNSIGNED, 
  customer_code INT NOT NULL, 
  PRIMARY KEY(sale_code), 
  INDEX(customer_code), 
  FOREIGN KEY(customer_code) REFERENCES customer(customer_code)
);
```

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
