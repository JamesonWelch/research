########
# Yahoo link is no longer available. Need alternatives
########
import json
from urllib.request import urlopen

with urlopen('https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json') as response:
    source = response.read()

data = json.loads(source)
#print(json.dumps(data, indent=2))

usd_rates = dict()

for item in data['list']['resources']:
    name = item['resources']['fields']['name']
    price = item['resources']['fields']['price']
    usd_rates[name] = price

print(50 * float(use_rates['USD/EUR']))
