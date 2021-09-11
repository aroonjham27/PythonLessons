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

def my_longName(name):
    x = " ".join(name)
    print(x)

myname = ["William", "Cherryflavor", "Longbottom", "Jr."]

my_longName(myname)
