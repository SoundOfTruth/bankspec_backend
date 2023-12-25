import psycopg2
from config import host, user, password, db_name
from parsers.vtb import vtb_office_cash_usd_buy, vtb_office_cash_usd_sell, vtb_office_noncash_usd_buy, vtb_office_noncash_usd_sell
from parsers.sovcom import sovcom_office_cash_usd_buy, sovcom_office_cash_usd_sell, sovcom_office_noncash_usd_buy, sovcom_office_noncash_usd_sell
from parsers.alfa import alfa_office_usd_buy, alfa_office_usd_sell
from parsers.gazprom import gazprom_office_cash_usd_buy, gazprom_office_cash_usd_sell, gazprom_office_noncash_usd_buy, gazprom_office_noncash_usd_sell


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    # insert data into a table
    with connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO office_cash_currency (name, usdbuy, usdsell) VALUES
            ('ВТБ', '{vtb_office_cash_usd_buy}', '{vtb_office_cash_usd_sell}');"""
            f"""INSERT INTO office_cash_currency (name, usdbuy, usdsell) VALUES
            ('Альфа-банк', '{alfa_office_usd_buy}', '{alfa_office_usd_sell}');"""
            f"""INSERT INTO office_cash_currency (name, usdbuy, usdsell) VALUES
            ('Совкомбанк', '{sovcom_office_cash_usd_buy}', '{sovcom_office_cash_usd_sell}');"""
            f"""INSERT INTO office_cash_currency (name, usdbuy, usdsell) VALUES
            ('Газпромбанк', '{gazprom_office_cash_usd_buy}', '{gazprom_office_cash_usd_sell}');"""
        )
    with connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO office_noncash_currency (name, usdbuy, usdsell) VALUES
                ('ВТБ', '{vtb_office_noncash_usd_buy}', '{vtb_office_noncash_usd_sell}');"""
            f"""INSERT INTO office_noncash_currency (name, usdbuy, usdsell) VALUES
                ('Альфа-банк', '{alfa_office_usd_buy}', '{alfa_office_usd_sell}');"""
            f"""INSERT INTO office_noncash_currency (name, usdbuy, usdsell) VALUES
                ('Совкомбанк', '{sovcom_office_noncash_usd_buy}', '{sovcom_office_noncash_usd_sell}');"""
            f"""INSERT INTO office_noncash_currency (name, usdbuy, usdsell) VALUES
                ('Газпромбанк', '{gazprom_office_noncash_usd_buy}', '{gazprom_office_noncash_usd_sell}');"""
            )
        print("[INFO] Data was succefully inserted")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")
