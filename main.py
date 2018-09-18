import time
from configparser import ConfigParser
from selenium import webdriver

# Initialize Config
config = ConfigParser()
config.read('config.ini')
aliExpressConfig = config['AliExpress']

# initialize Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome('driver/chromedriver', chrome_options=chrome_options)

driver.get(aliExpressConfig['WebsiteUrl'])
time.sleep(2)
search_box = driver.find_element_by_id('search-key')
search_box.send_keys('Iphone8')
search_box.submit()
time.sleep(5)
driver.quit()
