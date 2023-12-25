from parsers.vtb import vtb_office_cash_usd_buy, vtb_office_cash_usd_sell, vtb_office_noncash_usd_buy, vtb_office_noncash_usd_sell
from parsers.sovcom import sovcom_office_cash_usd_buy, sovcom_office_cash_usd_sell, sovcom_office_noncash_usd_buy, sovcom_office_noncash_usd_sell
from parsers.alfa import alfa_office_usd_buy, alfa_office_usd_sell
from parsers.gazprom import gazprom_office_cash_usd_buy, gazprom_office_cash_usd_sell, gazprom_office_noncash_usd_buy, gazprom_office_noncash_usd_sell


def create_tables(cursor):
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS office_cash_currency(
            id serial PRIMARY KEY,
            name varchar(50) NOT NULL,
            usdbuy decimal,
            usdsell  decimal);"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS office_noncash_currency(
            id serial PRIMARY KEY,
            name varchar(50) NOT NULL,
            usdbuy decimal,
            usdsell  decimal);"""
    )
    print("[INFO] Table created successfully")


def fill_tables(cursor):
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


def update_tables(cursor):
    cursor.execute(
        F"""UPDATE office_cash_currency SET usdbuy = {vtb_office_cash_usd_buy} WHERE name = 'ВТБ';"""
        F"""UPDATE office_cash_currency SET usdsell = {vtb_office_cash_usd_sell} WHERE name = 'ВТБ';"""
        F"""UPDATE office_cash_currency SET usdbuy = {alfa_office_usd_buy} WHERE name = 'Альфа-банк';"""
        F"""UPDATE office_cash_currency SET usdsell = {alfa_office_usd_sell} WHERE name = 'Альфа-банк';"""
        F"""UPDATE office_cash_currency SET usdbuy = {sovcom_office_cash_usd_buy} WHERE name = 'Совкомбанк';"""
        F"""UPDATE office_cash_currency SET usdsell = {sovcom_office_cash_usd_sell} WHERE name = 'Совкомбанк';"""
        F"""UPDATE office_cash_currency SET usdbuy = {gazprom_office_cash_usd_buy} WHERE name = 'Газпромбанк';"""
        F"""UPDATE office_cash_currency SET usdsell = {gazprom_office_cash_usd_sell} WHERE name = 'Газпромбанк';"""
    )
    cursor.execute(
        F"""UPDATE office_noncash_currency SET usdbuy = {vtb_office_noncash_usd_buy} WHERE name = 'ВТБ';"""
        F"""UPDATE office_noncash_currency SET usdsell = {vtb_office_noncash_usd_sell} WHERE name = 'ВТБ';"""
        F"""UPDATE office_noncash_currency SET usdbuy = {alfa_office_usd_buy} WHERE name = 'Альфа-банк';"""
        F"""UPDATE office_noncash_currency SET usdsell = {alfa_office_usd_sell} WHERE name = 'Альфа-банк';"""
        F"""UPDATE office_noncash_currency SET usdbuy = {sovcom_office_noncash_usd_buy} WHERE name = 'Совкомбанк';"""
        F"""UPDATE office_noncash_currency SET usdsell = {sovcom_office_noncash_usd_sell} WHERE name = 'Совкомбанк';"""
        F"""UPDATE office_noncash_currency SET usdbuy = {gazprom_office_noncash_usd_buy} WHERE name = 'Газпромбанк';"""
        F"""UPDATE office_noncash_currency SET usdsell = {gazprom_office_noncash_usd_sell} WHERE name = 'Газпромбанк';"""
    )
    print("[INFO] Data was succefully updated")


def fill_or_update_tables(cursor):
    cursor.execute("""SELECT * FROM office_cash_currency;""")
    check_empty = cursor.fetchall()
    if not check_empty:
        fill_tables(cursor)

    else:
        update_tables(cursor)