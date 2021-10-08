
# pip install sqlalchemy
# pip install psycopg2-binary

from sqlalchemy import create_engine
import os

# 1. connect to the RDS database

username = 'postgres'
password = os.getenv('RDS_PASSWORD')
port = '5432'
host = os.getenv('RDS_HOST')
database = 'northwind'

connection_string = f"postgres://{username}:{password}@{host}:{port}/{database}"
print(connection_string)

conn = create_engine(connection_string, echo=True)
print(conn)

# 2. execute the query
query = """
SELECT now(), orderID FROM orders;
"""
import pandas as pd

result = conn.execute(query)
df = pd.DataFrame(result)
print(df)

result = conn.execute(query)
data = list(result)

df = pd.read_sql(query, conn)

print(df.head(3))

