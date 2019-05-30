from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
#import pandas as pd
import os
from tabulate import tabulate
import json
from selenium.webdriver.firefox.options import Options as FirefoxOptions



#launch url
url = "https://www.pizzahut.lk/home"

labelList = ["PIZZAS"]

# create a new Firefox session

#Add option for headless browsing
options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

#driver = webdriver.Edge()
driver.implicitly_wait(30)
driver.get(url)

soup_level1=BeautifulSoup(driver.page_source, 'lxml')

x=1#counter
divsList = []

for index in labelList:

    pizzaDataList = [] #Empty list for store pizza data

    button = driver.find_element_by_link_text(index)
    print (str(x)+" "+button.get_attribute("href"))
    button.click()#go to the link

    tempPage=BeautifulSoup(driver.page_source, 'lxml')#Selenium hands of the source of the specific job page to Beautiful Soup

    #subMenuCategories = tempPage.find_all("ul",attrs={"class": "sub-menu-categories-ul"})#get sub category links and loop through each

    for subMenu in tempPage.find_all("ul",attrs={"class": "sub-menu-categories-ul"}):

        subMenuLinks = subMenu.find_all("li")
        numberOfLinksInSubMenu = len(subMenuLinks)
        print(numberOfLinksInSubMenu)

        for i,list in enumerate(subMenuLinks):
            a = list.find('a')  

            #print(a.get_attribute("class"))
            print("\n\t\t\t"+a['href'],a.get_text())

            subMenuPage = BeautifulSoup(driver.page_source,'lxml')#get the current page html block

            singleItemHolder = subMenuPage.find_all("div",attrs={"class" : "box"})
            print (len(singleItemHolder))

            for box in singleItemHolder:
               
                itemName = box.find("h3",attrs={"class":"menu-item-name hidden-lg hidden-md"})#get the name
                itemImageSrc = box.find("img",attrs={"alt":"image-name"})#get the image src
                itemDescription = box.find("p",attrs={"class":"hidden-xs hidden-sm menu-item-desc text-left"})#get the description

                pizzaData = {
                        'name': itemName.get_text(),
                        'src': itemImageSrc['src'],
                        'desc': itemDescription.get_text()
                            }
                
                pizzaData_json = json.dumps(pizzaData)#create a json string

                pizzaDataList.append(pizzaData_json)


            if i < (numberOfLinksInSubMenu-1): #handling the index out of range
                nextLink = subMenuLinks[i+1].find('a')
                driver.find_element_by_link_text(nextLink.get_text().upper()).click()
           
                #leave from the loop


   

    x += 1

print("\nNumber of pizzas: "+str(len(pizzaDataList)))

pizzaDataFinalJson = json.dumps(pizzaDataList)

#print ("\n"+ pizzaDataFinalJson)

path = os.getcwd()

#open, write, and close the file
f = open(path + "\\pizza_data_json.json","w") #FHSU
f.write(pizzaDataFinalJson)
f.close()

print("All done")
driver.quit()#quit the driver

#go to all the links in order now part

#python_button = driver.find_element_by_link_text('PIZZAS') #Go to the pizzas page
#python_button.click()


