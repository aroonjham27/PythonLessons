# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 15:19:25 2021

@author: 6041476
"""

def aot():
    height = int(input("What is the height of your triangle?\n"))
    base = int(input("What is the base of your triangle?\n"))
    print("the area of your triangle is ",str(0.5*height*base))
'''    
aot()

### function with arguments

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Aroon", "Jham") 

### function with arguments that have a default

def my_function(country = "Pluto"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil") 

#### function that takes list as an argument

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

## Another fun example 

def my_longName(name):
    x = " ".join(name)
    print(x)

myname = ["William", "Cherryflavor", "Longbottom", "Jr."]

my_longName(myname)

######### Part 2 ###################

## Introduction to *args. *operator unpacks an iterable

# option 1
def my_sum(a, b):
    return a + b

# option 2
def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [1, 2, 3]
print(my_sum(list_of_integers))

# option 3
def my_sum(*args):  
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))

#### introduction to **kwargs. **kwargs unpack

def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for x in kwargs.values():
        result += x
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
