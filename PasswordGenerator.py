# Method 1: using list

import random

mychars = ["A","B","C","D","E","F","a","b","c","d","e",
           "1","2","3","4","5","6","7","8","9","0","&","@","!","-","*","%"]

pw = ''
for i in range(8):
    
    mychar = random.choice(mychars)
    pw = pw+mychar
    
print(pw)

# Method 2: using random.choices
pw1 = random.choices(mychars,k=8)
pw1 = ''.join(pw1)
print(pw1)

# Method 3: using string

mychars2 = 'ABCDEFGHIabcdefgh1234567890@#$%^&*()'

pw3 = ''
for i in range(8):
    
    mychar = random.choice(mychars)
    pw3 = pw3+mychar
    
print(pw3)
