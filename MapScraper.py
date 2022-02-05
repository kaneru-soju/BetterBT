from datetime import datetime

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import threading

import MessageParser


class MapScraper():
    driver = None

    def __init__(self):
        PATH = "C:\\Users\\Aniruthan Ramadoss\\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get("https://ridebt.org/routes-schedules")

    def schedule_query(self, text_message):
        query_info = MessageParser.parse_message(text_message)
        parsed = [int(x) for x in query_info[3].split(':')]
        query_time = datetime.today().replace(hour=parsed[0], minute=parsed[1], second=0)
        delta = query_time - datetime.now()

        print(f'delta: {delta.seconds}')
        timer = threading.Timer(delta.seconds, self.query_routes, [query_info])
        timer.start()

        print('Scheduled!!!')

    def query_routes(self, query_information):
        stop_codes = {""}
        result = []
        if query_information[0] != "":
            self.driver.get("https://ridebt.org/routes-schedules" + f"?route={query_information[0]}")
            result = self.query_routes_with_bus()
        # if query_information[2] == "":



    def query_routes_with_bus(self):
        return None




scraper = MapScraper()
scraper.schedule_query("TOM, Torgersen Hall, 1114, 17:58")
