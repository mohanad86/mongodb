# MogoDB inserting data with python script
inserting Documents, Birthdates, Names

### Connecting to the database 

First start to connect to the database

- ssh -L 54321:172.16.0.71:27017 test@servername -p 22
- mongo localhost:54321
  

### Commands for mongoDB

```sh
$ show dbs
$ use selected.db
$ show tables
```

### Delete the database or tables

```sh
$ db.test.drop()
$ db.test.dropDatabase()
```
### Find and count data into the database

```sh
$ db.test.count();
$ db.test.find();
```

### Count by exacte name
```sh
$ db.test.find({"name":"Tom"}).count()
```

Author: Mohanad Aly

