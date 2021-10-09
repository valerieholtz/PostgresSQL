
## Goal: 

Creating a PostgreSQL database  and migrate it to Amazon RDS. Use Python/SQLAlchemy to insert data and query the database.

![image](https://user-images.githubusercontent.com/79086000/136655767-a86f51fd-9ec8-4616-a3d3-77d8aea6842d.png)

## Part 1:
This project should be seen as an example guide to set up a PostgresSQL on a local machine, create a database and load in data. Further to connect with the Database through SQLAlchemy via Python and be able to work with the data as a DataFrame. 

## Instructions:
- Get data from https://github.com/pawlodkowski/northwind_data_clean
— Install postgres on local machine
- Connect to postgres via psql -h <host> -U <user> 
- create database with CREATE DATABASE northwind;
- connect to a database with \c northwind
- Import northwind data by running \i create_database.sql over command line
- pip install sqlalchemy and psycopg2-binary and run PostgresSQL_SQLAlchemy.py to connect to database via sqlalchemy in python
- use database engine to run SQL queries and store the results in a Pandas DataFrame

## Part 2:
Repeat this process on the Cloud Computer AWS RDS. A pg_dump file is created that can be used to migrate the local database to the cloud databse. Further connect with the Database through SQLAlchemy via Python.

## Instructions:
- Create an AWS account and create a PostgreSQL DB instance on RDS
- create a pg_dump file from local northward database via pg_dump -U postgres --no-owner northwind > pg_dump.sql
- conncect to your AWS RDS via psql -h <remote-host> -U <user> and create a remote northward database
- run psql -f pg_dump.sql -h <remote-host> -U postgres -p 5432 -d <db-name>
- connect to postgres via sqlalchemy in python by running the program


## Keywords:

PostgresSQL

SQL

AWS

RDS

Python

SQLAlchemy

Cloud Computing
