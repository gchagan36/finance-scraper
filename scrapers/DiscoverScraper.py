import requests

from bs4 import BeautifulSoup
from selenium import webdriver

class DiscoverScraper:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.session = requests.Session()
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        self.options.add_argument("--headless")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(options=options, executable_path=["chromedriver.exe"])
        self.driver.implicitly_wait(15)

    def login(self):
        url = "https://portal.discover.com/customersvcs/universalLogin/ac_main"
        self.driver.get(url)
        username = self.driver.find_element_by_id("userid-content")
        password = self.driver.find_element_by_id("password-content")
        username.send_keys(self.username)
        password.send_keys(self.password)
        self.driver.find_element_by_id("log-in-button").click()