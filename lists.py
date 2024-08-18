# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 12:26:27 2021

@author: mehdiyeva
"""

#CHAPTER 8 - LISTS
"""As we want to solve more complex problems in Python, we need more powerful variables. 
Up to now we have been using simple variables to store numbers or strings where we have a single value in a variable. 
Starting with lists we will store many values in a single variable using an indexing scheme to store, organize, 
and retrieve different values from within a single variable. We call these multi-valued variables "collections" or "data structures"."""

family = ["dad", "siblings"]
for person in family: 
    print (person)
family.append("mom") #adding elements to the end of a list. Also, don't write x = x.append() for example, do not assign it to the variable
print (family)
print(family[2]) #accessing elements of a list 

family[0] = "Opa" #reassing elements in a list
print (family)

#The 'in' operator also works on lists:

"dad" in  family #outpus is always True or False.

#to write or update the elements, you need indices. A common way to do that is to combine the functions 'range' and 'len':
for i in range(len(family)): # len of the family after appending an element is 3; len returns the number of elements in the list
    family [i] = family[i] * 2
    print (family)

#LIST OPERATIONS:
a = [1,2,3]
b = [4,5,6]
print(a+b) # '+' operator concatenates lists
c = [3]
print(c*3) # '*' operator repeats a list a given number of times

#LIST SLICES:
s = a[2:] #same as in strings
print(s)

a[0:1] = [8] #a slice operator can update multiple elements. We updated element 1 with 8.
print(a)

#LIST METHODS:
#append is given above
a = [1,2,3]
b = [4,5,6]
a.extend(b) #takes a list as an argument and appends all of the elements; in other words, we extended list a adding list b to it.
print(a) 

f = ["y", "a", "i"]
f.sort() #arranges elements of a list from low to high
print(f)

#BEST FRIENDS: STRINGS AND LISTS
abc = 'with three words' #take a string
stuff = abc.split()      #split it and get a list of strings.
print(stuff)       
print(len(stuff))
print (stuff[1])
for s in stuff:  #runs 3 times and each time through it's with three words.
    print(s)

line = 'A lot               of spaces'
etc = line.split() # even though there's extra spaces here, when we split this line we still get four things; an extra space doesn't freak split out
print(etc)

line = 'first;second;third'
thing = line.split() #you can tell split to use a different delimiter. If we do it just this way, it's looking for spaces and it finds none.
print(thing) #And it doesn't realize these semicolons are what we want it to split
print (len(thing))

thing = line.split(';') #you can tell split to split based on a different character other than whitespace.
print(thing)
print(len(thing)) 

fhand = open ('mbox-short.txt')
for line in fhand:
    line = line.rstrip()       
    if not line.startswith('From: '): continue
    words = line.split()
    print(words[1])
       

#DOUBLE SPLIT
fhand = open ('mbox-short.txt')
for line in fhand:
    line = line.rstrip()       
    if not line.startswith('From: '): continue #find lines with From
    words = line.split()  #splits those lines into the words
    email = words[1]      #take emails
    pieces = email.split('@') #split emails from the specific character @
    #print(pieces)      
    print(pieces[1])  #gives us only the desired part after @

#fruit = 'Banana' #cannot be done since Banana here is not a list but string
#fruit[0] = 'b'
#print(fruit)

"""8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
The program should build a list of words. For each word on each line check to see if the word is already in the list 
and if not append it to the list.
When the program completes, sort and print the resulting words in alphabetical order."""
fname = input ('enter file name: ')
fhand = open (fname)
lst = list()
for line in fhand:
    line = line.rstrip()
    slines = line.split() #splitted lines
    #print(slines) #bu line ile split olunmush listi goruruk
    for word in slines: #For each word on each line check to see if the word is already in the list
        #if word in lst: continue  #this way or the one with 'not in', both works fine
        #else:
            #lst.append(word)
        if word not in lst:  #if the word is not in he list, append it to the list.
            lst.append(word)
lst.sort() #alphabetical ordering
print(lst)


fname = input ('Enter file name: ')
if len(fname) < 1:
    fname = "mbox-short.txt"
fhand = open (fname)
count = 0
for line in fhand:
    line = line.rstrip()
    #slines  = line.split()
    if not line.startswith('From '): continue  #alternatively: if slines[0]!='From ': continue
    count = count + 1
    slines  = line.split()
    #print(line, count)
    print(slines[1])
print ('There were', count, 'lines in the file with From as a firt word')

