import requests
import json

headers = {
    'authority': 'prod-api.sovcombank.ru',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru,en;q=0.9',
    'origin': 'https://sovcombank.ru',
    'referer': 'https://sovcombank.ru/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "YaBrowser";v="23"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.881 YaBrowser/23.9.2.881 Yowser/2.5 Safari/537.36',
}

cash_params = {
    'lang': 'ru',
    'type': 'FIZ_NAL',
    'departments': '7100360',
}

online_params = {
    'lang': 'ru',
    'type': 'FIZ_BEZNAL',
    'departments': '2760002',
}
response_cash = requests.get('https://prod-api.sovcombank.ru/service/currency-rate/index', params=cash_params, headers=headers)
response_noncash = requests.get('https://prod-api.sovcombank.ru/service/currency-rate/index', params=online_params, headers=headers)


if response_cash.status_code == 200:
    sovcom_cash_sell = []
    sovcom_cash_buy = []
    for i in range (len(response_cash.json())):
        sovcom_cash_sell.append(response_cash.json()[i]['buy'])
        sovcom_cash_buy.append(response_cash.json()[i]['sell'])
    sovcom_office_cash_usd_sell = float(sovcom_cash_sell[0])
    sovcom_office_cash_usd_buy = float(sovcom_cash_buy[0])


if response_noncash.status_code == 200:
    sovcom_noncash_sell = []
    sovcom_noncash_buy = []
    for i in range (len(response_noncash.json())):
        sovcom_noncash_sell.append(response_noncash.json()[i]['buy'])
        sovcom_noncash_buy.append(response_noncash.json()[i]['sell'])
    sovcom_office_noncash_usd_sell = sovcom_noncash_sell[0]
    sovcom_office_noncash_usd_buy = sovcom_noncash_buy[0]
