from selenium import webdriver
import bs4 as bs
import requests
from selenium.webdriver.support.ui import Select
import re
from time import sleep


base_url = 'http://www.supremenewyork.com/'
shop = 'shop/all/'
checkout = 'checkout/'

#入力フォーム
info = {
    "product": "GORE-TEX Overcoat",
    "color": "Black",
    "category": "jackets",
    "name": "内田",
    "email": "painlove@gmail.com",
    "phone": "080137069",
    "address": "2-2999 oooo06",
    "zip": "1620061",
    "number": "1234123412341234",
    "month": "09",
    "year": "2020",
    "ccv": "123",
}
#サイズ選択とカードの使用期限はプログラミング本体を設定してください。

options = webdriver.ChromeOptions()

#ここにUAを書きます。今回はiPhoneでsafari
options.add_argument('--user-agent='+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36")
options.add_argument('--user-data-dir=' + "/Users/uchidachihiro/sample/chrome")
driver = webdriver.Chrome(options=options,executable_path= "/Users/uchidachihiro/sample/chromedriver")
driver.delete_all_cookies()


r = requests.get(
    "{}{}{}".format(
        base_url,
        shop,
        info["category"])).text
        #リクエストモジュールでカテゴリーのURLをテキスト状態で取得
soup = bs.BeautifulSoup(r, "lxml")
#読み込んだテキストをLXML形式に変換してbeautifulsoup利用
temp_tuple = []

for link in soup.find_all("a",style=True):#カテゴリー画面から各商品のURLを検索、スタイルの間に存在している
    link_each = link.attrs["href"]#linkはタグ属性であるため独自の型が必要になってくる
    status = link.div
    if isinstance(status,type(None)):
        temp_tuple.append(link_each)

for link2 in temp_tuple:#各商品のURLからターゲットとなる商品を絞り込む
    r2 = requests.get(
        "{}{}".format(
        base_url,
        link2)).text
    soup2 = bs.BeautifulSoup(r2, "lxml")#
    title=soup2.title.string
    if info["color"] in title  and info["product"] in title :#タイトルにまとめて商品とカラーが記載されていたので両方一致したものを抽出する
        destination_url="{}{}".format(base_url,link2)#最

driver.get(destination_url)#サイトを立ち上げてリアルタイム処理開始
size = Select(driver.find_element_by_xpath('//*[@id="size"]'))#サイズ選択（ここのぴろグラムから直接いじる）：０＝SMALL、１＝MIDIUM、２＝LARGE
#size = Select(driver.find_element_by_name("size"))#サイズ選択（ここのぴろグラムから直接いじる）：０＝SMALL、１＝MIDIUM、２＝LARGE
size.select_by_index(1)
sleep(1)
driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()#カートインへ
sleep(2)#間隔調整　長いと確実
driver.get('http://www.supremenewyork.com/checkout')#決済画面へ
sleep(1)
driver.find_element_by_name('commit').click()
