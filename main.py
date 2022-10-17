import requests
res = requests.get('https://wikimedia.org/api/rest_v1/metrics/pageviews/top/pt.wikipedia/mobile-app/2015/11/01')
print(res)
res = requests.get('https://www.mediawiki.org/wiki/Special:MyLanguage/API:Lists')
print(res.json)
