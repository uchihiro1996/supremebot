import urllib.request from urllib as url
import bs4 from beautifulsoup as bs
import slack_notify from slack_notification

r1= url.urlopen("https://yeezysupply.com"),read()
html =bs(r1,'lmxl')
available=html.find_all("script",id="js-feature-json")
print(available)
