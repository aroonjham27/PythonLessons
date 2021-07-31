
"""
print and casting
"""

# a = 9
# print("the variable a = "+ a) # why does code not work?


"""
Random
"""

import random

random.randint(1,10)
random.randrange(1,15,step = 2) # does not include final endpoint
random.choice(["rock", "paper", "scissor"])
random.choices(["blue", "green", "orange","yellow"], k =2)

x = ["blue", "green", "orange","yellow"]
random.shuffle(x)

random.seed(123)
random.random()
random.uniform(1.0, 10.0)

"""
Python supports the following logical conditions:

    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b
"""

random.seed(123)

a = random.randint(1,10)
b = random.randint(1,10)
print("a = "+str(a))
print("b = "+str(b))
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
elif a > b:
  print("a is greater than b")

# the else statement

color = input("what is your favorite color?\n")
if color.lower() == "blue":
    print("The color of the sky, how beautiful")
elif color.lower() == "green":
    print("the color of life. How refreshing")
elif color.lower() == "yellow":
    print("the color fun and happiness. How wonderful")
elif color.lower() == "white":
    print("the color of purity. How noble")
elif color.lower() == "red":
    print("the color of valor. How strong")
else: print("nice color")

# And versus OR

import random 
a = random.randint(1,10)
b = random.randint(1,10)
c = random.randint(1,10)
print("a = "+str(a))
print("b = "+str(b))
print("c = "+str(c))

if a > b and a > c:
    print("both conditions are true")

if a > b or a > c:
  print("At least one of the conditions is True")

# example of nested if
x = int(input('Enter your age: '))

if x > 21:
    if x > 150:
        print('You must be a tree. You are at the wrong place')
    else:
        print('Welcome, you are of the right age!')
else:
    print('You are too young, go away!')






















myage = input("what is your age")
if myage > 11: 
    print("welcome")
elif myage > 15:
    print("not welcome")
else:
    print("not welcome")


























