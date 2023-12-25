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

    # Update data into a table
    with connection.cursor() as cursor:
        cursor.execute(
            F"""UPDATE office_cash_currency SET usdbuy = {vtb_office_cash_usd_buy} WHERE name = 'VTB';"""
            F"""UPDATE office_cash_currency SET usdsell = {vtb_office_cash_usd_sell} WHERE name = 'VTB';"""
            F"""UPDATE office_cash_currency SET usdbuy = {alfa_office_usd_buy} WHERE name = 'ALFA';"""
            F"""UPDATE office_cash_currency SET usdsell = {alfa_office_usd_sell} WHERE name = 'ALFA';"""
            F"""UPDATE office_cash_currency SET usdbuy = {sovcom_office_cash_usd_buy} WHERE name = 'SOVCOM';"""
            F"""UPDATE office_cash_currency SET usdsell = {sovcom_office_cash_usd_sell} WHERE name = 'SOVCOM';"""
            F"""UPDATE office_cash_currency SET usdbuy = {gazprom_office_cash_usd_buy} WHERE name = 'GAZPROM';"""
            F"""UPDATE office_cash_currency SET usdsell = {gazprom_office_cash_usd_sell} WHERE name = 'GAZPROM';"""
        )
    with connection.cursor() as cursor:
        cursor.execute(
            F"""UPDATE office_noncash_currency SET usdbuy = {vtb_office_noncash_usd_buy} WHERE name = 'VTB';"""
            F"""UPDATE office_noncash_currency SET usdsell = {vtb_office_noncash_usd_sell} WHERE name = 'VTB';"""
            F"""UPDATE office_noncash_currency SET usdbuy = {alfa_office_usd_buy} WHERE name = 'ALFA';"""
            F"""UPDATE office_noncash_currency SET usdsell = {alfa_office_usd_sell} WHERE name = 'ALFA';"""
            F"""UPDATE office_noncash_currency SET usdbuy = {sovcom_office_noncash_usd_buy} WHERE name = 'SOVCOM';"""
            F"""UPDATE office_noncash_currency SET usdsell = {sovcom_office_noncash_usd_sell} WHERE name = 'SOVCOM';"""
            F"""UPDATE office_noncash_currency SET usdbuy = {gazprom_office_noncash_usd_buy} WHERE name = 'GAZPROM';"""
            F"""UPDATE office_noncash_currency SET usdsell = {gazprom_office_noncash_usd_sell} WHERE name = 'GAZPROM';"""
        )
        print("[INFO] Data was succefully updated")


except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")