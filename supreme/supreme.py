import requests
import bs4 as bs
from splinter import Browser
from selenium import webdriver

base_url = 'http://www.supremenewyork.com/'
shop = 'shop/all/'
checkout = 'checkout/'
driver = webdriver.Chrome("/Users/uchidachihiro/sample/chromedriver")

r = requests.get(
    "{}{}{}".format(
        base_url,
        shop,
        'jackets')).text
soup = bs.BeautifulSoup(r, 'lxml')
temp_tuple = []
temp_tuple2 = []
temp_link = []

for link in soup.find_all('a', style=True):
    temp_tuple.append((link['href'], link.text))

for link2 in temp_tuple:
    if link2[1]=="":
        temp_tuple2.append(link2)
for link3 in temp_tuple2:
    r2 = requests.get(base_url,link3[0]).text
    soup2 = bs.BeautifulSoup(r2, 'lxml')
    for link4 in soup2.find_all(id="figure"):
        print(link4)
