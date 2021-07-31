'''
for loops
'''

# loop through a list

fruits = ["apples", "peaches", "cherries"]
for x in fruits:
  print("I like to eat",x)
  
# Looping Through a String
  
for x in "oranges":
  print(x)

# loop through a range
  
for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)
  
# using else in a for loop

for x in range(6):
  print(x)
else:
  print("Finally finished!") 

# using break in a for loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break


# using continue in a for loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# nested for loops
  
adj = ["red", "big", "tasty"]
fruits = ["apple", "tomato", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 