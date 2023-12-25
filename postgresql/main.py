import psycopg2
from config import host, user, password, db_name
from postgresql.sql_requests import create_tables, fill_or_update_tables


def fill_table():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        cursor = connection.cursor()
        # create a new tables
        create_tables(cursor)
        # fill or update tables
        fill_or_update_tables(cursor)

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)

    finally:
        if connection:
            connection.close()
            cursor.close()
            print("[INFO] PostgreSQL connection closed")
            return 1
    return 0


if __name__=="__main__":
    fill_table()
