
## Goal: 

Create a PostgreSQL database and migrate it to Amazon Relational Database Service (RDS). Use Python/SQLAlchemy to insert data and query the database.

![Bildschirmfoto 2021-10-04 um 12 35 38](https://user-images.githubusercontent.com/79086000/136656952-267487cf-0be5-4ace-989d-098239a66e65.png)


## Part 1:
This project should be seen as an example guide to set up a PostgresSQL on a local machine, create a database and load in data. Further to connect with the Database through SQLAlchemy via Python and be able to work with the data as a DataFrame. 

## Instructions:
- Get data from https://github.com/pawlodkowski/northwind_data_clean 
- Install postgres on local machine
- Connect to postgres
- create database with CREATE DATABASE northwind;
- connect to a database with \c northwind
- Import northwind data by running \i create_database.sql over command line
- pip install sqlalchemy and psycopg2-binary and run PostgresSQL_SQLAlchemy.py to connect to database via SQLAlchemy in Python
- use database engine to run SQL queries and store the results in a Pandas DataFrame

## Part 2:
Repeat this process on the Cloud Computer AWS RDS. A pg_dump file is created that can be used to migrate the local database to the cloud databse. Further connect with the database through SQLAlchemy via Python.

## Instructions:
- Create an AWS account with a PostgreSQL DB instance on RDS
- create a pg_dump file from local northwind database via pg_dump -U postgres northwind > pg_dump.sql
- conncect to your AWS RDS via psql -h 'remote-host' -U user and create a remote northwind database
- run psql -f pg_dump.sql -h 'remote-host' -U postgres -p 'port' -d 'db-name' to migrate the data to the remote database
- connect to remote database via SQLAlchemy in Python by running the program Amazon RDS_SQLAlchemy.py
- use program to run SQL queries and store the results in a Pandas DataFrame


## Keywords:

- PostgresSQL
- SQL
- AWS
- RDS
- Python
- SQLAlchemy
- Cloud Computing
