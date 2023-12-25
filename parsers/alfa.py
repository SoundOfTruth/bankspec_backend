import json
import requests
from bs4  import BeautifulSoup


#Альфабанк курсы валют в отделениях
alfa_office = requests.get(url="https://alfabank.ru/currency/")
alfa_officedata = BeautifulSoup(alfa_office.text, "html.parser")
alfa_officeblock = alfa_officedata.findAll("td", attrs={"align": "right"})

alfa_office_usd_sell = float(alfa_officeblock[0].text.replace(',', "."))
alfa_office_usd_buy = float(alfa_officeblock[1].text.replace(',', "."))


cookies = {
    'site_city': 'f73e6532/omsk',
    'last_tags_of_interest': '',
    'xpe': 'true',
    '_ym_uid': '1697101753208078650',
    '_ym_d': '1697101753',
    'alfa_ia_param_ya_cid': '1697101753208078650',
    'gtm_referrer': 'https://yandex.ru/',
    'ab_test_ao': 'ok',
    'prodID': 'Other',
    'tmr_lvid': '0129905749ef5b3ba31fd4fc43c6be3d',
    'tmr_lvidTS': '1697101753741',
    '__SourceTracker': 'yandex.ru__organic',
    'platformId': 'alfasite',
    'staduid': 'https%3A%2F%2Falfabank.ru%2Fcurrency%2F',
    'gtm-session-start': '1697173690729',
    '_sp_ses.3c2b': '*',
    '_ym_visorc': 'b',
    'stopTimer30secOnsite': '1',
    '_ym_isad': '2',
    'tmr_detect': '0%7C1697173952033',
    'RaQSvLavtfAf1aV3': '2b361cd6-e8b0-400c-bb15-ab39066670a8',
    'PageNumber': '4',
    '_sp_id.3c2b': '7e46029d-f848-44b3-8375-b8db48747cff.1697101754.4.1697173976.1697161808.3ea71ac6-2c12-4478-afb4-6198f2f29b81',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru,en;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'site_city=f73e6532/omsk; last_tags_of_interest=; xpe=true; _ym_uid=1697101753208078650; _ym_d=1697101753; alfa_ia_param_ya_cid=1697101753208078650; gtm_referrer=https://yandex.ru/; ab_test_ao=ok; prodID=Other; tmr_lvid=0129905749ef5b3ba31fd4fc43c6be3d; tmr_lvidTS=1697101753741; __SourceTracker=yandex.ru__organic; platformId=alfasite; staduid=https%3A%2F%2Falfabank.ru%2Fcurrency%2F; gtm-session-start=1697173690729; _sp_ses.3c2b=*; _ym_visorc=b; stopTimer30secOnsite=1; _ym_isad=2; tmr_detect=0%7C1697173952033; RaQSvLavtfAf1aV3=2b361cd6-e8b0-400c-bb15-ab39066670a8; PageNumber=4; _sp_id.3c2b=7e46029d-f848-44b3-8375-b8db48747cff.1697101754.4.1697173976.1697161808.3ea71ac6-2c12-4478-afb4-6198f2f29b81',
    'Referer': 'https://alfabank.ru/currency/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.891 YaBrowser/23.9.2.891 Yowser/2.5 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "YaBrowser";v="23"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
#Альфабанк онлайн курсы
alfa_online = requests.get(
    'https://alfabank.ru/api/v1/scrooge/currencies/alfa-rates?date.lte=2023-10-13T11:12:56%2B03:00&lastActualForDate.eq=true&clientType.eq=standardCC&rateType.in=rateCass,makeCash&currencyCode.in=RUR,USD,EUR,CNY,GBP,CHF,CZK,TRY',
    cookies=cookies,
    headers=headers,
)

alfa_onlinedata = alfa_online.json()
alfa_usdonlineblock = alfa_onlinedata["data"][3]["rateByClientType"][0]['ratesByType'][0]["lastActualRate"]
alfa_euronlineblock = alfa_onlinedata["data"][1]["rateByClientType"][0]['ratesByType'][0]["lastActualRate"]
#send_json({"usdsell":alfa_usdonlineblock["buy"]["originalValue"], "usdbuy": alfa_usdonlineblock["sell"]["originalValue"], "eursell":alfa_euronlineblock["buy"]["originalValue"], "eurbuy": alfa_euronlineblock["sell"]["originalValue"]})