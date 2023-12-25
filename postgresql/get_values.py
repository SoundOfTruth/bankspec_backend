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

    # get data from a table
    cursor = connection.cursor()
    cursor.execute("""SELECT name, usdbuy, usdsell FROM office_cash_currency;""")
    #cursor.execute("""SELECT name, usdbuy, usdsell FROM office_noncash_currency;""")
    print(cursor.fetchall())

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")