from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import threading

import MessageParser
import config


class MapScraper():
    def __init__(self):
        self.PATH = "C:/Users/Aniruthan Ramadoss/chromedriver.exe"
        self.s = Service(self.PATH)
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get("https://ridebt.org/routes-schedules")

    def schedule_query(self, text_message, client, user):
        query_info = MessageParser.parse_message(text_message)
        parsed = [int(x) for x in query_info[3].split(':')]
        query_time = datetime.today().replace(hour=parsed[0], minute=parsed[1], second=0)
        delta = query_time - datetime.now()

        print(f'delta: {delta.seconds}')
        timer = threading.Timer(delta.seconds, self.send_message, [query_info, client, user])
        timer.start()

        print('Scheduled!!!')

    def send_message(self, query_info, client, user):
        result = '\n'.join(self.query_routes(query_info))
        client.messages.create(from_=config.phone_number,
                               to=user,
                               body=result)

    def query_routes(self, query_information):
        bus, location, stop_code, _ = query_information

        result = []
        # Get Stopcode
        stop_code = self.bt_dict[location] if stop_code == "" else stop_code

        # If there is a bus specified
        result = self.query_routes_with_bus(bus, stop_code) if bus != "" else self.query_routes_with_stopcode(stop_code)

        return result

    def query_routes_with_bus(self, bus, stop_code):
        result = []
        self.driver.get("https://ridebt.org/routes-schedules" + f"?route={bus}")
        table = self.driver.find_element(By.CSS_SELECTOR, "#stopTable")

        for row in table.find_elements(By.CSS_SELECTOR, 'tr'):
            for cell in row.find_elements(By.CSS_SELECTOR, 'td'):
                if stop_code in cell.text:
                    result.append(cell.text.replace("\n", " "))
        self.driver.close()
        return result

    def query_routes_with_stopcode(self, stop_code):
        result = []
        self.driver.get("https://ridebt.org/routes-schedules" + f"?stop={stop_code}")
        table = self.driver.find_element(By.CSS_SELECTOR, "#bt_routes > table > tbody")

        for row in table.find_elements(By.CSS_SELECTOR, 'tr'):
            for cell in row.find_elements(By.CSS_SELECTOR, 'td'):
                result.append(cell.text.replace("\n", " "))
        self.driver.close()
        return result

    bt_dict = {'Newman Library': '1100',
               'Burruss Hall': '1101',
               'Davidson Hall': '1102',
               'West Campus/Perry Nbnd': '1103',
               'Old Security Bldg': '1104',
               'Stanger/Old Turner Wbnd': '1106',
               'Hutcheson Hall': '1107',
               'War Memorial Hall': '1108',
               'Squires Ebnd': '1110',
               'Alumni Mall Ebnd': '1111',
               'Alumni Mall Wbnd': '1112',
               'Squires Wbnd': '1113',
               'Torgersen Hall': '1114',
               'Wright House': '1115',
               'Litton Reaves Hall': '1116',
               'Overflow Lot Wbnd': '1117',
               'Oak Lane North': '1118',
               'Oak Lane South': '1119',
               'Overflow Lot Ebnd': '1120',
               'I Lot/Cage Sbnd': '1121',
               'McComas Hall': '1123',
               'Cassell Coliseum': '1124',
               'Tennis Courts': '1125',
               'Harper Hall': '1126',
               'Lane Stadium S Endzone Sbnd': '1127',
               'Lane Stadium S Endzone Nbnd': '1128',
               'Coliseum Parking Lot Sbnd': '1129',
               'Oak Lane Nbnd': '1130',
               'Bioinfomatics Bldg': '1131',
               'Prices Fork/Old Glade Wbnd': '1200',
               'Vet School Wbnd': '1201',
               'Prices Fork/Plantation Wbnd': '1202',
               'Prices Fork/Huntington Wbnd': '1203',
               'Hethwood Square on Hethwood': '1204',
               'Tall Oaks/Hethwood Ebnd': '1205',
               'Tall Oaks/Foxhunt Ebnd': '1206',
               'Tall Oaks/Heather Ebnd': '1207',
               'Tall Oaks/Foxtrail Sbnd': '1208',
               'Stroubles Cr': '1209',
               'Tall Oaks/Copper Croft Nbnd': '1211',
               'Heather/Tall Oaks Nbnd': '1212',
               'Heather/Plymouth Nbnd': '1213',
               'Heather/Huntington Nbnd': '1214',
               'Prices Fork/Huntington Ebnd': '1215',
               'Prices Fork/Plantation Ebnd': '1216',
               'Prices Fork/Old Glade Ebnd': '1218',
               'Tall Oaks/Colonial Sbnd': '1222',
               'Toms Creek/Winston Nbnd': '1300',
               'Gilbert Linkous Nbnd': '1301',
               'Toms Creek/Watson Nbnd': '1302',
               'Toms Creek/McBryde Nbnd': '1303',
               'Broce/Toms Creek Ebnd': '1304',
               'Progress/Broce Nbnd': '1305',
               'Progress/University Terr Nbnd': '1306',
               'Progress/Patrick Henry Nbnd': '1307',
               'The Village on Patrick Henry Wbnd': '1308',
               'Patrick Henry/Toms Creek Wbnd': '1309',
               'University City/Toms Creek Wbnd': '1310',
               'Shawnee on University City Wbnd': '1311',
               'Shawnee on University City Sbnd': '1312',
               'University City/Broce Sbnd': '1313',
               'University City/Glade Sbnd': '1314',
               'University Mall Sbnd': '1315',
               'University Mall Nbnd': '1316',
               'University City/Broce Nbnd': '1318',
               'Shawnee on University City Nbnd': '1319',
               'Shawnee on University City Ebnd': '1320',
               'University City/Toms Creek Ebnd': '1322',
               'Patrick Henry/Toms Creek Ebnd': '1323',
               'The Village on Patrick Henry Ebnd': '1324',
               'Patrick Henry/Progress Ebnd': '1325',
               'Progress/Hunt Club Sbnd': '1326',
               'Progress/University Terr Sbnd': '1327',
               'Progress/Broce Sbnd': '1328',
               'Progress/Watson Sbnd': '1340',
               'Main/Montgomery Nbnd': '1400',
               'Main/Lucas Nbnd S': '1401',
               'Lucas/Main Ebnd': '1402',
               'Lucas/Giles Ebnd': '1403',
               'Giles/Northview Nbnd': '1404',
               'Giles/Heights Nbnd': '1405',
               'Giles/Patrick Henry Nbnd': '1406',
               'Patrick Henry/Giles Wbnd': '1407',
               'Patrick Henry/Main Wbnd': '1408',
               '1500 North Main Nbnd': '1409',
               'Main/Giles Nbnd': '1410',
               'Main/Red Maple Nbnd': '1411',
               'Givens/Main Wbnd': '1412',
               'Whipple/Givens Sbnd': '1413',
               'Pheasant Run': '1414',
               'Seneca/Patrick Henry Sbnd': '1415',
               'Main/Patrick Henry Sbnd': '1416',
               '1200 North Main Sbnd': '1417',
               'Main/Northview Sbnd': '1418',
               'Main/Lucas Sbnd': '1419',
               'Main/Montgomery Sbnd': '1420',
               'Main/Kabrich Sbnd': '1421',
               'Main/Collegiate Ct Sbnd': '1422',
               'Main/Turner Sbnd': '1423',
               'Whipple/Courtney Sbnd': '1428',
               '1500 North Main Sbnd': '1429',
               'Main/Turner Nbnd': '1431',
               'Patrick Henry/Seneca Ebnd': '1434',
               'Whipple/Main Sbnd': '1435',
               'Roanoke/Church Ebnd': '1500',
               'Roanoke/Wharton Ebnd': '1501',
               'Roanoke/Rutledge Ebnd': '1502',
               'Roanoke/Woolwine Ebnd': '1503',
               'Harding/Silverleaf Ebnd': '1504',
               'Harding/Patrick Henry Ebnd': '1506',
               'Harding/Apperson Ebnd': '1507',
               'Harding/Vista Ebnd': '1508',
               'Harding/Roanoke Ebnd': '1509',
               'Ascot/Harding Ebnd': '1510',
               'Ascot/Hampton': '1511',
               'Ascot/Harding Wbnd': '1512',
               'Harding/Rucker Wbnd': '1513',
               'Harding/Sutton Wbnd': '1514',
               'Harding/Apperson Wbnd': '1515',
               'Harding/Patrick Henry Wbnd': '1516',
               'Harding/Silverleaf Wbnd': '1517',
               'Roanoke/Woolwine Wbnd': '1518',
               'Roanoke/Rutledge Wbnd': '1519',
               'Roanoke/Wharton Wbnd': '1520',
               'Roanoke/Penn Wbnd': '1521',
               'Main/Roanoke Sbnd': '1600',
               'Blacksburg Municipal Building': '1601',
               'Main/Eheart Sbnd': '1602',
               'Main/Eakin Sbnd': '1603',
               'Main/Airport Sbnd': '1605',
               'Main/Faystone Sbnd': '1606',
               'Gables Shopping Center': '1607',
               'Main/Landsdowne Sbnd': '1608',
               'Fairfax/Ellett Ebnd': '1609',
               'Fairfax/New Kent Ebnd': '1610',
               'New Kent/Loudon Ebnd': '1611',
               'New Kent/Sussex Ebnd': '1612',
               'Grissom/Nellies Cave Nbnd': '1613',
               'Marlington/Grissom Wbnd': '1614',
               'Marlington/Emerald Wbnd': '1615',
               'Marlington/Grayland Wbnd': '1616',
               'Main/Landsdowne Nbnd': '1618',
               'Main/Ardmore Nbnd': '1619',
               'Blacksburg Square': '1620',
               'Main/Cohee Nbnd': '1621',
               'Main/Sunset Nbnd': '1622',
               'Main/Graves Nbnd': '1623',
               'Main/Hemlock Nbnd': '1624',
               'Main/Eakin Nbnd': '1625',
               'Main/Clay Nbnd': '1626',
               'Main/Lee Nbnd': '1627',
               'Main St Post Office': '1628',
               'Main/Hemlock Sbnd': '1635',
               'Industrial Park/Transportation Res Ebnd': '1636',
               'Prosperity/Industrial Park Nbnd': '1637',
               'Professional Park Nbnd': '1638',
               'Main/King Sbnd': '1648',
               'Blacksburg Transit': '1649',
               'Commerce/Industrial Park Sbnd': '1650',
               'Industrial Park/Prosperity Wbnd': '1651',
               'Pratt Dr/Garvin Bldg Sbnd': '1701',
               'Pratt/Kraft Ebnd': '1702',
               'Airport': '1703',
               'Pratt Dr/Andrews Bldg Sbnd': '1705',
               'Kraft/Tech Center Dr Sbnd': '1706',
               'Pratt/Kraft Wbnd': '1707',
               'Pratt Dr/Garvin Bldg Nbnd': '1708',
               'Pratt Dr/Andrews Bldg Nbnd': '1709',
               'Kraft/Research Ctr Ebnd': '1710',
               'Research Ctr/Rimrock Sbnd': '1711',
               'Research Ctr/Rimrock Nbnd': '1712',
               'Research Ctr/N Knollwood Nbnd': '1713',
               'Kraft/Knowledgeworks 1 Bldg Sbnd': '1714',
               'Kraft/Moss Bldg Sbnd': '1715',
               'Research Ctr/S Knollwood Nbnd': '1716',
               'Research Ctr/Innovation Sbnd': '1719',
               'Research Ctr/Innovation Nbnd': '1722',
               'Innovation/Smoot Wbnd': '1724',
               'New River Valley Mall': '1800',
               'NRV Theatre': '1801',
               'Walmart': '1802',
               'Laurel/Sycamore Ebnd': '2202',
               'DMV on Arbor': '2204',
               'Post Office on Arbor': '2205',
               'Arbor/Market': '2206',
               'Market/Shoppers Way Sbnd': '2207',
               'Shoppers Way Wbnd': '2209',
               'Shoppers Way Ebnd': '2226'}

#
# scraper = MapScraper()
# scraper.schedule_query("TOM, Torgersen Hall, 1114, 20:31")
