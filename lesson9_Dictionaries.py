# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 07:55:47 2021

@author: 6041476
"""
'''
# the concept of key: value


mystudent = {
    "name": "Niharika",
    "age": 12,
    "favSubj": "Math",
    "favMovies": ["toy story", "zootopia", "The Hobbit"]
    }

mystudent2 = {
    "name": "Liya",
    "age": 12,
    "favSubj": "Baking",
    "favMovies": ["Soul", "Onward"]
    }

print(mystudent)

print(len(mystudent))

print(type(mystudent))

# accessing values of specific keys

x = mystudent["favMovies"]
print(x)

x = mystudent.get("favMovies")
print(x)

# get a list of keys

x = mystudent.keys()
print(x)

# get a list of all values

x = mystudent.values()
print(x)

# get a list of keys and values

x = mystudent.items()
print(x)

# does a key exist in a dictionary ... we use the word "in"

if "age" in mystudent:
    print("the key exists")
else: print("no such key")

if "toy story" in mystudent["favMovies"]:
    print("yay")
else: print("nay")


# an interesting dictionary

grilledBrocolliRecipe = {
    "cooktime": 15,
    "cost": 1.25,
    "ingredients": ["brocolli", "butter", "garlic powder", "sea salt"],
    "step1": "preheat oven to 300 F",
    "step2": "grill brocolli for 10 minutes",
    "step3": "apply some butter to the grilled brocolli",
    "step4": "sprinkle garlic powder and sea salt",
    "step5": "you may add some hot sause to the final product",
    "realRecipe": False
    }

# change a value in a dictionary

mystudent["age"] = 13

print(mystudent)

# add a new key to a dictionary

mystudent["favGame"] = "Assasin's Creed"
print(mystudent)

# remove a key from a dictionary

mystudent.pop("favGame")
print(mystudent)

'''
# looping through a dictionary

thisdict = {
    "student1": "Liya",
    "student2": "Niharika",
    "student3": "Vaishnavi"}


# Print all key names in the dictionary

for x in thisdict:
  print(x) 

for x in thisdict.keys():
  print(x) 

# Print all values in the dictionary, one by one
for x in thisdict:
  print(thisdict[x]) 
  
for x in thisdict.values():
  print(x) 
  
# Loop through both keys and values
  
for x, y in thisdict.items():
  print(x, y) 
  
# help() function revisited