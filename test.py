
import requests
from bs4 import BeautifulSoup


def get_html(url):
	r = requests.get(url)
	print('Status code', r.status_code)
	# print(r.content)
	return r.text
	

def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	res = soup.findAll('a', class_='slider-product__name')
	print(res)
	
	
def main():
	# html = get_html('https://wordpress.org/')
	html = get_html('https://www.dns-shop.ru/')
	# get_data(html)
	print(html)
	
main()
