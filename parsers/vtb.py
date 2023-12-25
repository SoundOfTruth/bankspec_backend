import json
import requests

headers = {
    'authority': 'siteapi.vtb.ru',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'origin': 'https://www.vtb.ru',
    'referer': 'https://www.vtb.ru/',
    'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60',
}

vtb_office_cash_params = {
    'category': '1',
    'type': '1',
}

vtb_office_noncash_params = {
    'category': '2',
    'type': '1',
}
vtb_app_params = {
    'category': '3',
    'type': '1',
}

vtb_office = requests.get('https://siteapi.vtb.ru/api/currencyrates/table', params=vtb_office_cash_params, headers=headers)
vtb_office_cash_rates = vtb_office.json()["rates"]

vtb_office_cash_usd_sell = float(vtb_office_cash_rates[0]["bid"])
vtb_office_cash_usd_buy = float(vtb_office_cash_rates[0]["offer"])


vtb_online = requests.get('https://siteapi.vtb.ru/api/currencyrates/table', params=vtb_office_noncash_params, headers=headers)
vtb_office_noncash_rates = vtb_online.json()["rates"]
vtb_office_noncash_usd_sell = float(vtb_office_noncash_rates[0]["bid"])
vtb_office_noncash_usd_buy = float(vtb_office_noncash_rates[0]["offer"])
