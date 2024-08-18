# -*- coding: utf-8 -*-
"""
Created on Sun May  2 00:13:22 2021

@author: mehdi
"""

#Coursera: Py4E-Data Structures
#construct a loop to look at each of the letters in a string individually:

fruit = 'banana'

x=len(fruit)

index = 0
while index < x:
    letter = fruit[index]
    print(index, letter)
    index=index+1
    
#alternatively use "for" loop, unless you actually need to know the position:

fruit = "banana"
for x in fruit:
 print(x)
    
# Looping and counting:
#This is a loop that loop through each letter in a string and counts the number of times the loop encounters the 'a' character:
    
fruit = 'banana'
count = 0
for letter in fruit:
    if letter == 'a':
     count = count + 1
print (count)

#Slicing Strings: Monty Python

s = 'Monty Python'
print (s[0:4]) #from 0 up to 4, 4 is not including

print (s[:])
print (s[:3])
print (s[6:])