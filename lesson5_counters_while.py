# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 10:08:06 2020

@author: 6041476
"""
# Counters

i = 5

i += 1
i += 2
i += 3

print(i)

i -= 1
i -= 2
i -= 3

print(i)

# try i *=3

# the while loop

i = 1
while i < 6:
  print(i)
  i += 1
  
# while with else
  
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  
# continue
  
i = 0
while i < 60:
  i += 1
  if i%2 != 0:
    continue
  print(i)
  
# break
# breaks allow you to exit a loop

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1