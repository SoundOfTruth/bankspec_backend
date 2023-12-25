import psycopg2
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from config import host, user, password, db_name
from functions import send_data
from postgresql.main import fill_table
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/office_cash")
async def read_root():
    try:
        fill_table()
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
        data = cursor.fetchall()
        return send_data(data)
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")


@app.get("/office_noncash")
async def read_root():
    try:
        fill_table()
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        # get data from a table
        cursor = connection.cursor()
        cursor.execute("""SELECT name, usdbuy, usdsell FROM office_noncash_currency;""")
        data = cursor.fetchall()
        return send_data(data)
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")


@app.get("/refrash_tables")
async def read_root():
    check = fill_table()
    if check == 1:
        return 1
    else:
        return 0