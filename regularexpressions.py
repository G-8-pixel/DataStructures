# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 14:48:43 2021

@author: mehdi
"""
"""Regular expressions are a cryptic but powerful language for matching strings and extracting elements from those strings"""
#REGULAR EXPRESSIONS
#USING re.search() like startswith():
import re 
hand = open ('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line): # ^ means 'From' at the beginning; it matchs the starts of a line
        print(line)
#Matching and Extracting Data
x = 'My favorite 2 numbers are 19 and 32'
y = re.findall('[0-9]+', x) #[0-9] is one or more digits. If we want the matching strings to be extrcated, we use re.findall().
y = re.findall('[AODEF]', x) #there is no matching string, so this gives an empty list
print(y)  #gives us a list of numbers
