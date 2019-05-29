import json
import os

pizzaDict = {
    'name': 'Cheese Pizza',
    'description': 'This is a cheese pizza',
    'price': 'Rs.890'
}

pizza_json = json.dumps(pizzaDict)
print (pizzaDict)

path = os.getcwd()
f = open(path + "\\pizza_json.json","w") #FHSU
f.write(pizza_json)
f.close()

print(path)