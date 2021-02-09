from selenium import webdriver
import bs4 as bs
import requests
import re

driver = webdriver.Chrome(executable_path= "/Users/uchidachihiro/sample/chromedriver")
r = requests.get(
    "https://www.supremenewyork.com/shop/jackets/zxqalywpc/op7f2j6id").text
soup = bs.BeautifulSoup(r, "lxml")
print(soup.title.string)
if "GORE-TEX Court Jacket" in soup.title.string and "Red" in soup.title.string:
    color_cloth=soup.find_all("option")
    for i in color_cloth:
        num = re.sub("\\D","", r"%s"%i)
        print(num)    # "2019"
sleep(5)
driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()


#カラー選択スクリプト置き場
if info["color"] in soup2.title.string  and info["product"] in soup2.title.string :
    destination_url="{}{}".format(base_url,link2)
    color_cloth=soup2.find_all("option")
    for i in color_cloth:
        num = re.sub("\\D","", r"%s"%i)
        temp_size.append(num)




driver.get(destination_url)
color_element = driver.find_element_by_name("size")

# 取得したエレメントをSelectタグに対応したエレメントに変化させる
color_select_element = Select(color_element)

# 選択したいvalueを指定する
color_select_element.select_by_value(temp_size[info["size"]])
