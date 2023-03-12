
import requests

res = requests.get('https://api.coingecko.com/api/v3/ping').json()
print(res)