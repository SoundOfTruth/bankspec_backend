import requests
import json


headers = {
    'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.gazprombank.ru/personal/courses/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60',
    'credentials': 'include',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'cityId': '295',
    'version': '3',
    'ab_version': 'original',
}
# webapp curr
#with open("gazprom.json", "w", encoding="utf-8") as file:
    #json.dump(gazprom.json(), file, indent=4, ensure_ascii=False)
#gazprom_online = gazprom.json()[1]
#gazprom_online_data = gazprom_online["content"][0]["items"]
#send_json({"usdsell":gazprom_online_data[0]["buy"], "usdbuy": gazprom_online_data[0]["sell"],"eursell":gazprom_online_data[1]["buy"], "eurbuy": gazprom_online_data[1]["sell"]})


gazprom = requests.get('https://www.gazprombank.ru/rest/exchange/rate', params=params, headers=headers)
gazprom_office_cash = gazprom.json()[2]
gazprom_office_cash_data = gazprom_office_cash["content"][0]["items"]
#send_json({"usdsell":gazprom_office_cash_data[0]["buy"], "usdbuy": gazprom_office_cash_data[0]["sell"],"eursell":gazprom_office_cash_data[1]["buy"], "eurbuy": gazprom_office_cash_data[1]["sell"]})
gazprom_office_cash_usd_sell = gazprom_office_cash_data[0]["buy"]
gazprom_office_cash_usd_buy = gazprom_office_cash_data[0]["sell"]

gazprom_office_noncash = gazprom.json()[3]
gazprom_office_noncash_data = gazprom_office_noncash["content"]["segment_regular"][0]["items"]
#send_json({"usdsell":gazprom_office_noncash_data[0]["buy"], "usdbuy": gazprom_office_noncash_data[0]["sell"],"eursell":gazprom_office_noncash_data[1]["buy"], "eurbuy": gazprom_office_noncash_data[1]["sell"]})
gazprom_office_noncash_usd_sell = gazprom_office_noncash_data[0]["buy"]
gazprom_office_noncash_usd_buy = gazprom_office_noncash_data[0]["sell"]