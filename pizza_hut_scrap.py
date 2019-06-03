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
#options = FirefoxOptions()options=options
#options.add_argument("--headless")
driver = webdriver.Firefox()

#driver = webdriver.Edge()
driver.implicitly_wait(30)
driver.get(url)

soup_level1=BeautifulSoup(driver.page_source, 'lxml')

x=1#counter
divsList = []
popularDealsListImages = []
AllPromos = [] #store all the promotion images
pizzaDataList = [] #Empty list for store pizza data

def getThePopularDeals():
    #store popular deals images

    promoDivs = soup_level1.find_all("div",attrs={"class":"col-md-6 col-sm-12 col-xs-12 promo-single promo-add"})

    numberOfpopularDeals = len(promoDivs)
    print("Number of popular deals: "+str(numberOfpopularDeals))

    for promos in promoDivs:

        singleImage = promos.find("img",attrs={"class","img img-responsive"})
        popularDealsListImages.append(singleImage['src'])
    
    print("Number of images : "+str(len(popularDealsListImages)))
   

def getAllThePromos():
   

    url = "https://www.pizzahut.lk/menu/promo/meal-deal"
    driver.implicitly_wait(30)
    driver.get(url)

    allThePromosPage=BeautifulSoup(driver.page_source, 'lxml')
    items = allThePromosPage.find_all("div",attrs={"class","itemContainer promo-item"})

    print("Number of all promos : "+str(len(items)))

    for i,item in enumerate(items) :
       
        name = item.find("h3",attrs={"class":"menu-item-name"})['data-original-title']
    
        image = item.find("img",attrs={"alt":name})
        price = item.find("span",attrs={"class":"hidden-sm hidden-xs"})
        details = item.find("p",attrs = {"class":"menu-item-desc hidden-sm hidden-xs"})

        singleItem = {
            "name": name,
            "price":price.get_text().replace('\\n', ''),
            "desc":details.get_text(),
            "src": image['src']
        }

    
        AllPromos.append(singleItem)



def getPizzaData():
    url = "https://www.pizzahut.lk/home"
    driver.implicitly_wait(30)
    driver.get(url)
    x=0


    for index in labelList:

        button = driver.find_element_by_link_text(index)
        print (button.get_attribute("href"))
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
                
                    pizzaDataList.append(pizzaData)


                if i < (numberOfLinksInSubMenu-1): #handling the index out of range
                    nextLink = subMenuLinks[i+1].find('a')
                    driver.find_element_by_link_text(nextLink.get_text().upper()).click()
           
            #leave from the loop
                
        

    print("\nNumber of pizzas: "+str(len(pizzaDataList)))

   

    #print ("\n"+ pizzaDataFinalJson)




getThePopularDeals()
getAllThePromos()
getPizzaData()

imageJson = json.dumps(popularDealsListImages)
allPromosJson = json.dumps(AllPromos)
pizzaDataFinalJson = json.dumps(pizzaDataList)

path = os.getcwd()

#open, write, and close the file
f = open(path + "\\pizza_data.json","w") #FHSU
f.write(pizzaDataFinalJson)
f.close()

f = open(path + "\\popular_deals.json","w") #FHSU
f.write(imageJson)
f.close()

f = open(path + "\\all_promos.json","w") #FHSU
f.write(allPromosJson)
f.close()

print("All done")
driver.quit()#quit the driver

#go to all the links in order now part

#python_button = driver.find_element_by_link_text('PIZZAS') #Go to the pizzas page
#  python_button.click()
