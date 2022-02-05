from datetime import datetime

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import threading

import MessageParser


class MapScraper():
    # PATH = "C:\\Users\\Aniruthan Ramadoss\\chromedriver.exe"
    # driver = webdriver.Chrome(PATH)
    # driver.get("https://ridebt.org/routes-schedules")

    def schedule_query(self, text_message):
        query_info = MessageParser.parse_message(text_message)
        parsed = [int(x) for x in query_info[3].split(':')]
        query_time = datetime.today().replace(hour=parsed[0], minute=parsed[1], second=0)
        delta = query_time - datetime.now()

        print(f'delta: {delta.seconds}')
        timer = threading.Timer(delta.seconds, self.query_routes, [text_message])
        timer.start()

        print('Scheduled!!!')

    def query_routes(self, text_message):
        print(f'method called with args: {text_message}')


scraper = MapScraper()
scraper.schedule_query("TOM, Torgersen Hall, 1114, 17:58")
