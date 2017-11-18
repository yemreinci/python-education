import requests as rq
import re

eksiurl = 'https://eksisozluk.com/'

res = rq.get(eksiurl)

pattern = '<a\s+href=".+\?a=popular">(.+) <small>[0-9]+<\/small><\/a>'

matches = re.findall(pattern, res.text)

for s in matches:
    print(s)
