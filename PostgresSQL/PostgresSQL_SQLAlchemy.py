#!pip install SQLAlchemy 
#!pip install psycopg2
#!pip install psycopg2-binary

import pandas as pd
import sqlalchemy
import os

HOST = 'localhost'
PORT = '5432'
DATABASE = 'northwind'  
USER = 'postgres'
PASSWORD = os.getenv('PSQL_PASSWORD')

conn_string = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

#  Whenever we want to use SQLAlchemy to interact with a database, we need to create an Engine.

engine = sqlalchemy.create_engine(conn_string, echo=False)
 
query = 'SELECT * FROM northwind LIMIT 5;'

pd.read_sql(query, engine)