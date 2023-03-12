
import requests

res = requests.get(  'https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=usd').json()
print(res)