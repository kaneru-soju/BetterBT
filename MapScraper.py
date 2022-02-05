from datetime import datetime

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import threading

import MessageParser

bt_dict = {'1100': 'Newman Library',
           '1101': 'Burruss Hall',
           '1102': 'Davidson Hall',
           '1103': 'West Campus/Perry Nbnd',
           '1104': 'Old Security Bldg',
           '1106': 'Stanger/Old Turner Wbnd',
           '1107': 'Hutcheson Hall',
           '1108': 'War Memorial Hall',
           '1110': 'Squires Ebnd',
           '1111': 'Alumni Mall Ebnd',
           '1112': 'Alumni Mall Wbnd',
           '1113': 'Squires Wbnd',
           '1114': 'Torgersen Hall',
           '1115': 'Wright House',
           '1116': 'Litton Reaves Hall',
           '1117': 'Overflow Lot Wbnd',
           '1118': 'Oak Lane North',
           '1119': 'Oak Lane South',
           '1120': 'Overflow Lot Ebnd',
           '1121': 'I Lot/Cage Sbnd',
           '1123': 'McComas Hall',
           '1124': 'Cassell Coliseum',
           '1125': 'Tennis Courts',
           '1126': 'Harper Hall',
           '1127': 'Lane Stadium S Endzone Sbnd',
           '1128': 'Lane Stadium S Endzone Nbnd',
           '1129': 'Coliseum Parking Lot Sbnd',
           '1130': 'Oak Lane Nbnd',
           '1131': 'Bioinfomatics Bldg',
           '1200': 'Prices Fork/Old Glade Wbnd',
           '1201': 'Vet School Wbnd',
           '1202': 'Prices Fork/Plantation Wbnd',
           '1203': 'Prices Fork/Huntington Wbnd',
           '1204': 'Hethwood Square on Hethwood',
           '1205': 'Tall Oaks/Hethwood Ebnd',
           '1206': 'Tall Oaks/Foxhunt Ebnd',
           '1207': 'Tall Oaks/Heather Ebnd',
           '1208': 'Tall Oaks/Foxtrail Sbnd',
           '1209': 'Stroubles Cr',
           '1211': 'Tall Oaks/Copper Croft Nbnd',
           '1212': 'Heather/Tall Oaks Nbnd',
           '1213': 'Heather/Plymouth Nbnd',
           '1214': 'Heather/Huntington Nbnd',
           '1215': 'Prices Fork/Huntington Ebnd',
           '1216': 'Prices Fork/Plantation Ebnd',
           '1218': 'Prices Fork/Old Glade Ebnd',
           '1222': 'Tall Oaks/Colonial Sbnd',
           '1300': 'Toms Creek/Winston Nbnd',
           '1301': 'Gilbert Linkous Nbnd',
           '1302': 'Toms Creek/Watson Nbnd',
           '1303': 'Toms Creek/McBryde Nbnd',
           '1304': 'Broce/Toms Creek Ebnd',
           '1305': 'Progress/Broce Nbnd',
           '1306': 'Progress/University Terr Nbnd',
           '1307': 'Progress/Patrick Henry Nbnd',
           '1308': 'The Village on Patrick Henry Wbnd',
           '1309': 'Patrick Henry/Toms Creek Wbnd',
           '1310': 'University City/Toms Creek Wbnd',
           '1311': 'Shawnee on University City Wbnd',
           '1312': 'Shawnee on University City Sbnd',
           '1313': 'University City/Broce Sbnd',
           '1314': 'University City/Glade Sbnd',
           '1315': 'University Mall Sbnd',
           '1316': 'University Mall Nbnd',
           '1318': 'University City/Broce Nbnd',
           '1319': 'Shawnee on University City Nbnd',
           '1320': 'Shawnee on University City Ebnd',
           '1322': 'University City/Toms Creek Ebnd',
           '1323': 'Patrick Henry/Toms Creek Ebnd',
           '1324': 'The Village on Patrick Henry Ebnd',
           '1325': 'Patrick Henry/Progress Ebnd',
           '1326': 'Progress/Hunt Club Sbnd',
           '1327': 'Progress/University Terr Sbnd',
           '1328': 'Progress/Broce Sbnd',
           '1340': 'Progress/Watson Sbnd',
           '1400': 'Main/Montgomery Nbnd',
           '1401': 'Main/Lucas Nbnd S',
           '1402': 'Lucas/Main Ebnd',
           '1403': 'Lucas/Giles Ebnd',
           '1404': 'Giles/Northview Nbnd',
           '1405': 'Giles/Heights Nbnd',
           '1406': 'Giles/Patrick Henry Nbnd',
           '1407': 'Patrick Henry/Giles Wbnd',
           '1408': 'Patrick Henry/Main Wbnd',
           '1409': '1500 North Main Nbnd',
           '1410': 'Main/Giles Nbnd',
           '1411': 'Main/Red Maple Nbnd',
           '1412': 'Givens/Main Wbnd',
           '1413': 'Whipple/Givens Sbnd',
           '1414': 'Pheasant Run',
           '1415': 'Seneca/Patrick Henry Sbnd',
           '1416': 'Main/Patrick Henry Sbnd',
           '1417': '1200 North Main Sbnd',
           '1418': 'Main/Northview Sbnd',
           '1419': 'Main/Lucas Sbnd',
           '1420': 'Main/Montgomery Sbnd',
           '1421': 'Main/Kabrich Sbnd',
           '1422': 'Main/Collegiate Ct Sbnd',
           '1423': 'Main/Turner Sbnd',
           '1428': 'Whipple/Courtney Sbnd',
           '1429': '1500 North Main Sbnd',
           '1431': 'Main/Turner Nbnd',
           '1434': 'Patrick Henry/Seneca Ebnd',
           '1435': 'Whipple/Main Sbnd',
           '1500': 'Roanoke/Church Ebnd',
           '1501': 'Roanoke/Wharton Ebnd',
           '1502': 'Roanoke/Rutledge Ebnd',
           '1503': 'Roanoke/Woolwine Ebnd',
           '1504': 'Harding/Silverleaf Ebnd',
           '1506': 'Harding/Patrick Henry Ebnd',
           '1507': 'Harding/Apperson Ebnd',
           '1508': 'Harding/Vista Ebnd',
           '1509': 'Harding/Roanoke Ebnd',
           '1510': 'Ascot/Harding Ebnd',
           '1511': 'Ascot/Hampton',
           '1512': 'Ascot/Harding Wbnd',
           '1513': 'Harding/Rucker Wbnd',
           '1514': 'Harding/Sutton Wbnd',
           '1515': 'Harding/Apperson Wbnd',
           '1516': 'Harding/Patrick Henry Wbnd',
           '1517': 'Harding/Silverleaf Wbnd',
           '1518': 'Roanoke/Woolwine Wbnd',
           '1519': 'Roanoke/Rutledge Wbnd',
           '1520': 'Roanoke/Wharton Wbnd',
           '1521': 'Roanoke/Penn Wbnd',
           '1600': 'Main/Roanoke Sbnd',
           '1601': 'Blacksburg Municipal Building',
           '1602': 'Main/Eheart Sbnd',
           '1603': 'Main/Eakin Sbnd',
           '1605': 'Main/Airport Sbnd',
           '1606': 'Main/Faystone Sbnd',
           '1607': 'Gables Shopping Center',
           '1608': 'Main/Landsdowne Sbnd',
           '1609': 'Fairfax/Ellett Ebnd',
           '1610': 'Fairfax/New Kent Ebnd',
           '1611': 'New Kent/Loudon Ebnd',
           '1612': 'New Kent/Sussex Ebnd',
           '1613': 'Grissom/Nellies Cave Nbnd',
           '1614': 'Marlington/Grissom Wbnd',
           '1615': 'Marlington/Emerald Wbnd',
           '1616': 'Marlington/Grayland Wbnd',
           '1618': 'Main/Landsdowne Nbnd',
           '1619': 'Main/Ardmore Nbnd',
           '1620': 'Blacksburg Square',
           '1621': 'Main/Cohee Nbnd',
           '1622': 'Main/Sunset Nbnd',
           '1623': 'Main/Graves Nbnd',
           '1624': 'Main/Hemlock Nbnd',
           '1625': 'Main/Eakin Nbnd',
           '1626': 'Main/Clay Nbnd',
           '1627': 'Main/Lee Nbnd',
           '1628': 'Main St Post Office',
           '1635': 'Main/Hemlock Sbnd',
           '1636': 'Industrial Park/Transportation Res Ebnd',
           '1637': 'Prosperity/Industrial Park Nbnd',
           '1638': 'Professional Park Nbnd',
           '1648': 'Main/King Sbnd',
           '1649': 'Blacksburg Transit',
           '1650': 'Commerce/Industrial Park Sbnd',
           '1651': 'Industrial Park/Prosperity Wbnd',
           '1701': 'Pratt Dr/Garvin Bldg Sbnd',
           '1702': 'Pratt/Kraft Ebnd',
           '1703': 'Airport',
           '1705': 'Pratt Dr/Andrews Bldg Sbnd',
           '1706': 'Kraft/Tech Center Dr Sbnd',
           '1707': 'Pratt/Kraft Wbnd',
           '1708': 'Pratt Dr/Garvin Bldg Nbnd',
           '1709': 'Pratt Dr/Andrews Bldg Nbnd',
           '1710': 'Kraft/Research Ctr Ebnd',
           '1711': 'Research Ctr/Rimrock Sbnd',
           '1712': 'Research Ctr/Rimrock Nbnd',
           '1713': 'Research Ctr/N Knollwood Nbnd',
           '1714': 'Kraft/Knowledgeworks 1 Bldg Sbnd',
           '1715': 'Kraft/Moss Bldg Sbnd',
           '1716': 'Research Ctr/S Knollwood Nbnd',
           '1719': 'Research Ctr/Innovation Sbnd',
           '1722': 'Research Ctr/Innovation Nbnd',
           '1724': 'Innovation/Smoot Wbnd',
           '1800': 'New River Valley Mall',
           '1801': 'NRV Theatre',
           '1802': 'Walmart',
           '2202': 'Laurel/Sycamore Ebnd',
           '2204': 'DMV on Arbor',
           '2205': 'Post Office on Arbor',
           '2206': 'Arbor/Market',
           '2207': 'Market/Shoppers Way Sbnd',
           '2209': 'Shoppers Way Wbnd',
           '2226': 'Shoppers Way Ebnd'}


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
