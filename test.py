import requests
import json
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}
ret = requests.post(url, data=json.dumps(payload),headers=headers)
print(ret.url)
print(ret.text)

https://design-patterns.readthedocs.io/zh_CN/latest/creational_patterns/simple_factory.html

