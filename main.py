import requests


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

res = requests.get('https://wikimedia.org/api/rest_v1/metrics/pageviews/top/fr.wikipedia/all-access/2022/10/15'
, headers=headers)
print(res.status_code)
