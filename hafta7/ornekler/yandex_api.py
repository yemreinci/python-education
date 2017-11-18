import requests as rq
import json


api_key = '<YOUR_KEY_HERE>' # Buraya yandex'in size verdigi key'i yazin. 'trnsl' ile baslayan uzunca bir string. Rastgele harfler ve rakamlardan olusuyor.


def translate_to(text, lang):
    params = {
        'key': api_key,
        'text': text,
        'lang': lang
    }

    res = rq.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=params)

    return json.loads(res.text)['text'][0]

lang = input('Hedef dili girin: ') # Iki harfli kisaltma seklinde olmali. Mesela tr, en, ar, ...
# Yandex'in destekledigi dillerin tam listesi : https://tech.yandex.com/translate/doc/dg/concepts/api-overview-docpage/
while True:
  text = input('Metni girin: ')
  print(translate_to(text, lang))
