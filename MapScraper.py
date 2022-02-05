from datetime import datetime

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import MessageParser


class MapScraper():
    PATH = "C:\\Users\\Aniruthan Ramadoss\\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://ridebt.org/routes-schedules")
    
    def query_routes(self, text_message):
        query_info = MessageParser.parse_message(text_message)
        datetime.now().strftime('%X') == text_message[3]



