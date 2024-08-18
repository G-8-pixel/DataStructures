# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 22:12:20 2021

@author: mehdiyeva
"""
#CHAPTER 9: DICTIONARIES
"""The Python dictionary is one of its most powerful data structures. 
Instead of representing values in a linear list, dictionaries store data as key / value pairs. 
Using key / value pairs gives us a simple in-memory "database" in a single Python variable. Dictionaries are like bags-no order
Question 6
What is a common use of Python dictionaries in a program? --> Building a histogram counting the occurrences of various strings in a file"""

#stuff = dict()
#print (stuff['candy']) #output gives error since the dictionary is empty, and key has no corresponding value-
#print (stuff.get('candy', -1))
purse = dict () #make me an empty dictionary
purse['money'] = 12 #12 is the value, we're putting it into purse, but we're storing it under 'money'
purse['candy'] = 3
purse['tissiues'] = 75
print(purse)
print(purse['candy']) #to pull something out
purse['candy'] = purse['candy'] + 2 
print(purse)

#COMPARING LISTS AND DICTIONARIES
lst = list()
lst.append(21)
lst.append(234)
print(lst) #it will print 21 and 234 in order in the list
lst[0] = 23
print (lst)

ddd = dict()
ddd['age'] = 34
ddd['course'] = 222
print(ddd) #things will be not in order in the dictionary
ddd['age'] = 23
print(ddd)

#MANY COUNTERS WITH A DICTIONARY
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['csev'] = ccc['csev'] + 1
print(ccc)

#DICTIONARY TRACEBACKS: we can use the 'in' operator to see if a key is in the dictionary
ccc = dict()
#print(ccc['sdiv']) #traceback will appear here, since there is no 'sdiv' in the dictionary, we can check it with 'in' in the console writing: 'sdiv' in ccc

counts = dict()
names = ['Gunay', 'Aygun', 'Nigar', 'Aygun']
for name in names:
    if name not in counts:    #eger ki o listdeki adlar dictionaryde hec yoxdursa, 1 yaz, ilk defe cixib qabagimiza yeni. #Add new ones
        counts[name] = 1     
    else:
        counts[name] = counts[name] + 1 # eger dict.de varsa, o olanin ustune de 1 elave et #updates the existing ones
    #counts[name] = counts.get(name, 0) + 1 #butov if statementine alternative olaraq sadece bu line'i yazmaq olar, daha kompakt
print(counts)

#the get() method for Dictionaries
counts = dict()
names = ['Gunay', 'Aygun', 'Nigar', 'Aygun']
for name in names:
   if name in counts:
      x = counts[name]
   else:
      x = 0
#alternatively: 
#x = counts.get(name, 0) - only one line instead of 4 lines in if statement
print(counts)

#COUNTING PATTERN
counts = dict()
print('Enter a line of text:')
line = input('') #let the user enter the lines of text
words = line.split() #split those lines into words
print('WORDS', words) #get the LIST of words
print('Counting: ')  
for word in words:
    counts[word] = counts.get(word, 0) + 1 #count words in the dictionary; if there is no word in the dictionary, set its count to 0 and add 1. It means before there was 0 of that word, now 1.
print('Counts', counts)

#Definite loops and Dictionaries
counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print(key, counts[key]) #print keys and counts of those keys. Keys are the strings in the dictionary counts, values are the corresponding values to those keys

#Retrieving lists of Keys and Values: You can get a list of keys, values, or items (both) from a dictionary.
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(list(jjj))
print(jjj.keys())    #keys() method
print(jjj.values())  #values() method
print(jjj.items())   #items() method; output from this has 3 items, and each item is called TUPLE which we'll talk about later.
print(len(jjj.items()))

#Two iteration variables
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}  
for a, b in jjj.items(): #a for keys, b for corresponding values. This is a very convenient way to go through a dictionary and see all the key-value pairs.
    print(a, b)
#exercise
name = input ('Enter a file name: ')
fhand = open(name)
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
bigcount = None #biggest count we have seen so far
bigword = None  #biggest word that is associated with that biggest count 
for word, count in counts.items():  #here, word variable is going to go through all the keys and count is goinf to go through all the values
    if bigcount is None or count > bigcount:  #which means we are on the first word, OR the count we are looking at is bigger than the previous value, then remember it.
        bigword = word #we are remembering the word and count
        bigcount = count
print ('Word:', bigword,'\nCount:', bigcount)
    
"""Assignment 9.4: Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer."""

name = input("Enter file: ")
if len(name) < 1: #we do this so that we can just hit Enter and it defaults to "mbox-short.txt". If I want to give it a different name I can. 
                  #So if I just hit Enter at this prompt then this will give me a string that's zero length. So if it's less than 1 I'll just assume that         
    name = "mbox-short.txt"
#try:
handle = open(name)
#except:
    #print('No such file was found, try a different name', name)
    #exit()
lst = list()
for line in handle:  #reading through file
    if not line.startswith('From '): continue #in this line, if you don't use space after From, code works (counts) wrong. But, why?
    words = line.split()  #splitting lines into words
    #print(words) # list of words starting with 'From'
    lst.append(words[1]) #append the second words of the lines to the empty list, which are the email addresses. Now our list is not empty anymore.
    #w = words[1]
print(lst) # list of words

counts = dict() 
for email in lst:   #now we have to count occurance of email addresses using dictionary
     counts[email] = counts.get(email, 0) + 1 
       #if email in counts:
            #counts[email]+= 1
        #else:
            #counts[email]= 1
print('dictionary: ', counts)

bigcount = None 
bigword = None
scount = None
sword = None
for word, count in counts.items():    #word as key, count as corresponding value of the dictionary
        if bigcount == None or count > bigcount:
            bigcount = count
            bigword = word
        else:
            scount = count
            sword = word
print (bigword, bigcount)
print (sword, scount)
    