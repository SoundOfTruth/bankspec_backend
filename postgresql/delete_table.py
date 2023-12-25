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

    # delete a table
    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE IF EXISTS office_cash_currency;"""
        )
    # delete a table
    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE IF EXISTS office_noncash_currency;"""
        )
        print("[INFO] Table was deleted")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")