from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
#import pandas as pd
import os
from tabulate import tabulate
import json
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from lxml import etree
print("This is the lxml version: "  +etree.__version__)

#launch url
url = "https://www.pizzahut.lk/home"

labelList = ["PIZZAS"]

# create a new Firefox session

#Add option for headless browsing
#options = FirefoxOptions()
#options.add_argument("--headless")
driver = webdriver.Firefox()

driver.get('https://www.google.es/')



#driver.set_input_value('//input[@id="lst-ib"]', '21 buttons')

#driver.click('//center//img[@alt="Google"]')
#time.sleep(0.5)

#driver.click('//input[@name="btnK"]')
#time.sleep(0.5)

#first_google_result_title = driver.get_inner_html('(//div[@class="rc"]//a)[1]')





print("All done")
driver.quit()#quit the driver

#go to all the links in order now part

#python_button = driver.find_element_by_link_text('PIZZAS') #Go to the pizzas page
#python_button.click()