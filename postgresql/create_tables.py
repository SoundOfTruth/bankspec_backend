import psycopg2
from config import host, user, password, db_name

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    # create a new table
    with connection.cursor() as cursor:
        cursor.execute(
             """CREATE TABLE IF NOT EXISTS office_cash_currency(
                 id serial PRIMARY KEY,
                 name varchar(50) NOT NULL,
                 usdbuy decimal,
                 usdsell  decimal);"""
         )
    with connection.cursor() as cursor:
        cursor.execute(
             """CREATE TABLE IF NOT EXISTS office_noncash_currency(
                 id serial PRIMARY KEY,
                 name varchar(50) NOT NULL,
                 usdbuy decimal,
                 usdsell  decimal);"""
         )
    print("[INFO] Table created successfully")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)

finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
