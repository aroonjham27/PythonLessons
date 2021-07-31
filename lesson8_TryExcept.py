
weapons = ['axe', 'sword', 'mace', 'spear']
lowdamage = [3,5,4,1]
highdamage = [10,8,9,12]

print("here are your choice of weapons.\n")
print(weapons)

'''
choice = input("choose your weapon.\n")
choiceindex = weapons.index(choice.lower())
'''

import random

try:
    choice = input("choose your weapon\n")
    choiceindex = weapons.index(choice)
    a = lowdamage[choiceindex]
    b = highdamage[choiceindex]
    
    damage = random.randint(a,b)
    
    print("you deal a damage of "+str(damage))
    
except:
    print("Since you cannot read ... You are dead. The monster eats you for breakfast")

