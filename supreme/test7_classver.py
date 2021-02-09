from selenium import webdriver
import bs4 as bs
import requests
from selenium.webdriver.support.ui import Select
import re
from time import sleep

class supreme():
    def __init__(self):
        self.info={
        "product": "Backpack",
        "color": "Black",
        "category": "bags",
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
        self.base_url='http://www.supremenewyork.com/'
        self.shop='shop/all/'
        self.checkout='checkout/'

    def driver_chrome(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=self.options,executable_path= "/Users/uchidachihiro/sample/chromedriver")
        self.driver.delete_all_cookies()


    def stock_check(self):
        while True:
            try:
                r = requests.get(
                    "{}{}{}".format(
                        self.base_url,
                        self.shop,
                        self.info["category"])).text
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
                        self.base_url,
                        link2)).text
                    soup2 = bs.BeautifulSoup(r2, "lxml")#
                    title=soup2.title.string
                    if self.info["color"] in title  and self.info["product"] in title :#タイトルにまとめて商品とカラーが記載されていたので両方一致したものを抽出する
                        self.destination_url="{}{}".format(self.base_url,link2)#最


                return print(self.destination_url)


                break
            except:
                sleep(1)
                driver.refresh()



    def select_stuff_detail(self):
        self.driver.get(self.destination_url)#サイトを立ち上げてリアルタイム処理開始
        while True:
            try:
                size = Select(self.driver.find_element_by_xpath('//*[@id="size"]'))#サイズ選択（ここのぴろグラムから直接いじる）：０＝SMALL、１＝MIDIUM、２＝LARGE
                #size = Select(driver.find_element_by_name("size"))#サイズ選択（ここのぴろグラムから直接いじる）：０＝SMALL、１＝MIDIUM、２＝LARGE
                size.select_by_index(1)
                sleep(0.5)
                self.driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()#カートインへ

            except:
                sleep(0.5)
                self.driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()#カートインへ

            finally:
                sleep(0.5)#間隔調整　長いと確実
                self.driver.get('http://www.supremenewyork.com/checkout')#決済画面へ
            break

reac=supreme()
reac.driver_chrome()
reac.stock_check()
reac.select_stuff_detail()
