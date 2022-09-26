from distutils.log import Log
from re import search
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import sys
from pathlib import Path
from GoogleSheet import GoogleSheets

Order_post = 'PG14'
 
#Site
URL = 'https://www.myacg.com.tw/index.php'

OUTPUT_PATH = Path(__file__).parent.parent

def relative_to_assets(path: str) -> Path:
    return OUTPUT_PATH / Path(path)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

#Chrome Crawler Setting
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})
options.add_experimental_option("detach", True)

#Open Web
"""driver = webdriver.Chrome(relative_to_assets('chromedriver.exe'), options=options)
driver.get(URL)"""


class MYACG:
    def __init__(self, account, password):
        self.account = account
        self.password = password

        #Open Web
        global driver 
        driver = webdriver.Chrome(relative_to_assets('chromedriver.exe'), options=options)
        driver.get(URL)

        #find search bar and search ""
        Login_btn = driver.find_element(by = By.XPATH, value='//*[@id="header"]/div[1]/div/ul/li[2]/a')
        Login_btn.click()

        account_element = driver.find_element(by = By.NAME, value="account")
        password_element = driver.find_element(by = By.NAME, value="password")

        account_element.clear()
        password_element.clear()

        account_element.send_keys(self.account)
        password_element.send_keys(self.password)

        Login_btn = driver.find_element(by = By.XPATH, value = '//*[@id="form1"]/div/div/div[2]/div[5]/div[1]/a')
        Login_btn.click()

    def put_order_num(self, order_num = ''):
        """order_num: put order number in from entry"""
        self.order_num = Order_post + order_num
        Google = GoogleSheets(order_number=self.order_num, status= 'DONE')
        Google.appendWorksheet()
        print('DONE')

    def quit(self):
        """exit the webdriver"""
        print('QUIT')
        driver.quit()


    def run(self):
        print("done")
        
if __name__ == "__main__":
    pass
