# SQLDoctor: A Payload Fuzzing SQL Injection Tool 
SQLDoctor is a framework for the testing of SQL and NoSQL Injection. It supports: 
 

- SAP SYBASE 
- Teradata
- ADABAS
- MySQL
- FileMaker
- Microsoft Access
- Informix
- SQLite
- PostgreSQL
- Toad
- phpMyAdmin
- SQL Developer
- Sequel PRO
- Cloudera
- MariaDB
- Informix Dynamic Servers
- 4D
- Ingres SQL
- Amazon Aurora
- MongoDB
- Hadoop HDFS
- Robomongo
- OrientDB
- Neo4j
- CouchDB
- Redis
- Couchbase

---

## Usage
All URLs passed to SQLDoctor as arguments should be encased in quotation marks for reliable functionality.

### **Brute Forcing**
Running SQLDoctor without the `-f` flag will use the Brute Force payloads with no fuzzing. This execution mode supports two types of parsing:

1. HTML Parsing
2. URL Parsing 

 **HTML Parsing** does not need a flag. Just supply SQLDoctor with a URL to use as its target.

        ./Main.py [Target URL]

 **URL Parsing** allows SQLDoctor to parse the url for any injectable fields. For the cases where HTML parsing is not relevant you can supply the URL parsing flag `-u` to change the parsing method to this type:

    ./Main.py -u [Target URL]

### **Fuzzing**

Running SQLDoctor with the `-f` flag utilizes the payload fuzzer. To run this type:
    
    ./Main.py -f [Target URL]

For more _help_ with running enter -h or -help for usage examples and flags/options available

---

### Legal Disclaimer
 Any and all exploits present here are used at the discretion of the user. Additionally, it is the user's responsibility to obey all applicable law local, state and federal.
 All developers involved assume no liability and are not responsible for misuse or damage due to the use of this software. 

 Latest Version can be found at https://github.com/Mustard1/SQLsUCK




