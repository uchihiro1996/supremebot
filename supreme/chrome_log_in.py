
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=' + "/Users/uchidachihiro/sample/chrome")

driver = webdriver.Chrome(options=options,executable_path= "/Users/uchidachihiro/sample/chromedriver")
