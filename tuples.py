# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 00:06:40 2021

@author: mehdiyeva
"""

"""Tuples are our third and final basic Python data structure. Tuples are a simple version of lists. 
We often use tuples in conjunction with dictionaries to accomplish multi-step tasks like sorting or 
looping through all of the data in a dictionary. Tuples are not changeable"""
x = ('Gunay', 'Aysel', 'Inci')
print(x[2])

y = (1, 6, 10)
print (max(y))
for iter in y:
    print(iter)
    
#Tuples are not changeable:
x = [2, 3, 9] #lists are changeable
x[1] = 5
print(x)

#z = (5, 4, 1)
#z[0] = 2
#print(z) #we'll recieve traceback, since z is a Tuple and not mutable

#Things can't be done with Tuples. Whatever order you put the tuple in when you create it, it stays in that. You can't append, you can't extend it, you can't flip it with a reverse.
#Tuples and Assignment:
(x, y) = (4, 'fred') #putting a tuple on the LHS of an assignment statement. 
print(y)
print(x)

#(x, y) = 9 #this gonna blow up. Bc if there is a tupl on LHS, it wants a tuple on RHS too.

#TUPLES and DICTIONARIES
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (key, value) in d.items():  
    print(key, value)
print(d.items()) #items() method in Dictionaries returns a List of (key, value) Tuples

#TUPLES are COMPARABLE
(0,1,2) < (5,1,2)
(0, 1, 20000) < (0, 3, 4) #if the 1st item is equal, Python goes on the next element, until it finds elements that differ.Check this in Console
('Gunay', 'Sally') < ('Gunay', 'Sam')

#Sorting Lists of Tuples:
d = {'a':10, 'c':1, 'b':22}
print (d.items())
tupl = d.items()
s = sorted(tupl) #sort a list of tuples to get a sorted version of the dictionary
print(s) #it sorts the dict. based on the first thing(in this case based on 'keys') and give back a list. Btw, in dictionaries, you can't have two same keys. 
#sort by Keys in a dictionary
for k, v in s:
    print (k, v) 

#Sort by Values instead of Keys:
dic = {'a':10, 'c':1, 'b':22}   
lst = list()
for key, value in dic.items(): #dic.items() gives us list of tuples; so for k and v in this list, we append them to the empty list other way around (v, k)
    lst.append((value, key)) #things in the lists are tuples
print(sorted(lst)) #sort from low to high
lst = sorted(lst, reverse = True) #go backwards,so sort from high to low.
print(lst)

#In the previous chapter, we did the most common word. But now we want the ten most common words.
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
#print(counts)

lst = list()
for k, v in counts.items():
    lst.append((v, k))
lst = sorted(lst, reverse=True)
#lst.sort(reverse=True) #works in a same way like right above line
#print (sorted ([(v, k) for k, v in counts.items()], reverse=True))
print(lst)

for v, k in lst[:10]:
    print(k, v)
    
#Even shorter version:
dic = {'a':10, 'c':1, 'b':22}  
print (sorted ([(v, k) for k, v in dic.items()], reverse=True)) #instead of 4 lines of code above#list comprehension


"""Assignment 10.2: Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below."""
name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
lst = list()
for line in handle:
    if not line.startswith('From '): continue      
    words = line.split()
    #print(words)
    h = words[5]
    hrs = h.split(':')
    #print (hrs) 
    lst.append(hrs[0])
    lst.sort()
#print(lst)  #unsorted list of hours
#now it is time to count them:
counts = dict()
for hour in lst:
    counts[hour] = counts.get(hour, 0) + 1
#print(counts)

for (hours, count) in counts.items():
    print(hours, count)
#print(sorted([(hours, count) for (hours, count) in counts.items()]))

    