# HBNB - MySQL
## Introduction

This document describes how the HBnB project integrates a relational database, specifically MySQL, and uses SQLAlchemy as its ORM (Object Relational Mapper) to manipulate data efficiently. It provides a deep understanding of how models in the project are linked and how data is mapped to SQLAlchemy tables.

## The Relational Database

In the HBnB project, the database system used is MySQL. It is set up and structured using two SQL scripts:
- `setup_mysql_dev.sql` for development purposes
- `setup_mysql_test.sql` for testing purposes

These scripts are responsible for:
1. Creating the necessary databases.
2. Creating user accounts for these databases.
3. Granting appropriate permissions to these users.

## Object Relational Mapping (ORM) - SQLAlchemy


The ORM (Object-Relational Mapping) lets you interact with your database, like you would with SQL. In other words, it's a way to retrieve and store object data in a relational database seamlessly. An ORM does this by mapping the objects to the database tables.

Benefits of using an ORM:
1. **Abstraction of Tables**: Tables are represented as classes, and rows are instances of those classes.
2. **Database Agnostic**: Write code without worrying about the underlying database system.
3. **Reduce Boilerplate**: No need to write repetitive SQL code.
4. **Safe from SQL Injections**: Helps protect the database from common threats.

### SQLAlchemy in HBnB

SQLAlchemy is the chosen ORM for the HBnB project. It provides a set of high-level API to connect and interact with relational databases. Thus, you can think of SQLAlchemy as a bridge between Python and relational databases.

The main components we deal with in SQLAlchemy are:
- **Engine**: It is the starting point for any SQLAlchemy application. It's “home base” for the actual database and its DBAPI, which is delivered to the SQLAlchemy application through a connection pool and a dialect.
- **Session**: It is a holding zone for all the objects which you've loaded or associated with it during its lifespan. It provides the entryway to send commands to the database using the ORM.

In the HBnB project, these components are set up and managed in [`db_storage.py`](https://github.com/tim-ngeno/AirBnB_clone_v2/blob/master/models/engine/db_storage.py)

## Models and their Linkage

### BaseModel

All models in the HBnB project inherit from the `BaseModel` class. It ensures that essential attributes like `id`, `created_at`, and `updated_at` are initialized for every object. The `BaseModel` also integrates methods to convert objects to dictionaries (`to_dict`), save objects to storage (`save`), and delete them (`delete`).

### Other Models

Here's how other models are defined and linked:

1. **User**: Represents the users of the HBnB platform. It has attributes like `email`, `password`, `first_name`, and `last_name`. It has relationships with `Place` and `Review`, meaning a user can have multiple places and reviews.

2. **State**: Represents states. It has a relationship with `City`, meaning a state can have multiple cities.

3. **City**: Represents cities. It is associated with a `State` using a foreign key `state_id`. It also has relationships with `Place`, meaning a city can have multiple places.

4. **Place**: Represents places, which are essentially the listings in the HBnB platform. It has relationships with `City` and `User` through `city_id` and `user_id` respectively. It also has an attribute `amenity_ids` which is a list of `Amenity` objects associated with the place. 

5. **Review**: Represents reviews for places. It is associated with a `User` and a `Place` using foreign keys `user_id` and `place_id` respectively.

6. **Amenity**: Represents amenities, and it's linked with `Place` through a many-to-many relationship using the `place_amenity` table.

### Data Mapping to SQLAlchemy Tables

Every model is mapped to an SQLAlchemy table using the `Base` class from SQLAlchemy. The class variable `__tablename__` denotes the name of the table in the database. Attributes in the model classes are represented using SQLAlchemy's `Column`, and relationships between tables (like ForeignKey relationships) are also defined using SQLAlchemy constructs.

## Data Persistence in the Database

The persistence of data in the HBnB project is managed using the `save` method. When an object's `save` method is invoked, the following happens:
1. The object's `updated_at` attribute is updated to the current datetime.
2. The object is added to the session if it's a new object.
3. All changes (including additions and modifications) in the session are committed to the database.

## Conclusion

Using SQLAlchemy as an ORM in the HBnB project has made it possible to abstract the intricacies of dealing directly with a relational database. The well-defined models and their relationships, combined with the ORM, have made data manipulation tasks seamless, efficient, and secure.



---
# 0x03. AirBnB clone - Deploy static

## Table of Contents
1. [Introduction to Fabric](#introduction-to-fabric)
2. [Deploying Code to Servers](#deploying-code-to-servers)
3. [Understanding tgz Archives](#understanding-tgz-archives)
4. [Executing Fabric Commands](#executing-fabric-commands)
5. [Managing Nginx Configuration](#managing-nginx-configuration)
6. [Distinguishing Between `root` and `alias` in Nginx](#distinguishing-between-root-and-alias-in-nginx)

---

### 1. Introduction to Fabric

**Fabric** is a high-level Python (2.7 through 3.4+) library designed to simplify the execution of shell commands remotely over SSH. It provides a suite of basic operations and uses them as the building blocks for creating more complex workflows. With Fabric:

- Streamlining application deployment becomes straightforward.
- Configuration management gets centralized.
- Task automation is at your fingertips.

---

### 2. Deploying Code to Servers 

Deploying your application or script to a server should be a routine and error-free process. Here's how you can achieve that with Fabric:

1. **Create a `fabfile.py`**: This is where you'll store your tasks and commands.
2. **Execute with `fab`**: Once your tasks are defined, running them is as simple as invoking the `fab` command.

Fabric provides seamless error handling, parallel execution, and intricate execution strategies, making the deployment process efficient and reliable.

---

### 3. Understanding tgz Archives

A **tgz archive**, known by its full name as `.tar.gz`, is a fusion of TAR and GZIP. Here's the breakdown:

- **TAR (Tape Archive)**: Originally designed for tape drives, it groups multiple files into a single file, making it easier to handle.
  
- **GZIP (GNU Zip)**: This is a compression utility, which takes a TAR archive and reduces its size.

When you combine both, you get a `.tgz` or `.tar.gz` archive: a bundled and compressed set of files that is both portable and space-efficient.

---

### 4. Executing Fabric Commands 

Using Fabric commands is straightforward. Here's how:

**Locally**:
```bash
fab -H localhost your_task_name
```
Executing tasks locally helps in testing them before deployment to a live server.

**Remotely**:
```bash
fab -H remote_server_ip your_task_name
```
<<<<<<< HEAD
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
<br>
=======
This ensures that the task is executed on a specified remote server, making deployments and remote management a breeze.

---

### 5. Managing Nginx Configuration

Nginx is one of the most popular web servers, and managing its configuration is crucial for performance and security. Here's a look at managing configurations using Fabric:

1. **Transfer Configuration**: With Fabric, you can easily transfer updated configurations to remote servers.
   
2. **Apply Changes**: After updating the configuration, you'd typically need to reload or restart Nginx to apply those changes. 

Fabric streamlines these steps, making server management efficient and reducing the risk of manual errors.

---

### 6. Distinguishing Between `root` and `alias` in Nginx

Navigating the nuances of Nginx configuration can be tricky. Here's a clarification on two commonly misunderstood directives:

- **root**: Defines the root directory for the current request. If set as `root /var/www/html;`, a request to `http://yourserver/image.jpg` would look for `/var/www/html/image.jpg`.

- **alias**: This provides a direct replacement of the URI path. For instance, with `location /images/ { alias /var/graphics/; }`, a request to `http://yourserver/images/image.jpg` fetches `/var/graphics/image.jpg`.

The key distinction is how each directive interprets the location path. With `root`, the path is appended to the root directory, whereas `alias` directly maps the location path to a filesystem path.

---
>>>>>>> 87db89e6174899890009429bb5f13ce818055d4f
