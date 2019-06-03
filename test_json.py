import json
import os


pizzaDict = {
        'name': 'Cheese Pizza',
        'description': 'This is a cheese pizza',
        'price': 'Rs.890'
}

    

def createTheJson(pizzaDict):
    pizza_json = json.dumps(pizzaDict)
    return pizza_json

def printTheJson(jsonString):
    print (jsonString)

def createAndSaveTheFile(pizza_json):
    path = os.getcwd()
    f = open(path + "\\pizza_json.json","w") #FHSU
    f.write(pizza_json)
    f.close()

    print(path)
    

theJson = createTheJson(pizzaDict = pizzaDict)
printTheJson(jsonString = theJson)
createAndSaveTheFile(pizza_json = theJson)


    


    











