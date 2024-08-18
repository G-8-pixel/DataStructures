# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 00:32:50 2021

@author: mehdiyeva
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

#String concatenation
a = 'Hello'
b = a + 'There'
print(b)
c = a + ' ' + 'There'
print(c)

fruit = 'banana'

'n' in fruit

'm' in fruit

'nan' in fruit

if 'f' in fruit:
    print('Found it!')
else:
    print('Check it again!') 

#String comparison
word = 'banan'
if word == 'banana':
    print ('All right, bananas.')
if word < 'banana':
    print ('Your word, ' + word + ', comes before banana' )
elif word > 'banana':
    print('Your word,' + word + ', comes after banana' )
else:
    print('All right, bananas.')
        
#String Library
greet = 'Hello Gunay'
zap = greet.lower()  
print(zap)
print(greet)
print('Hi, there'.lower())

"""Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
Convert the extracted value to a floating point number and print it out."""

text = "X-DSPAM-Confidence:    0.8475"

startingIndex = text.find("0.8475") #we first find whats the starting point of the substring we want to exclude
number = text[startingIndex:] #then, to extract that substring we use slicing
f = float (number) #converting of the extracted number to the float
print (f)

#Can also be written as:
    
text = "X-DSPAM-Confidence: 0.8475"
f = float(text[text.find("0.8475"):])
print (f)

#Can also be written as:
text = "X-DSPAM-Confidence: 0.8475"
ipos = text.find(':')
value = float(text[ipos+2:])
print(value)

#newline, newline in line of files represents "enter".
smth = "Hello\nGunay"
print (smth)
len(smth) #if we ask how many characters in it with len, it gives 11 characters, including "\n".

xfile = open ('mbox.txt') #xfile is not a data, it is the way to get the data; file handle 
for cheese in xfile:
    print(cheese)

#counting lines in a file
fhand = open ('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print ('Line Count:', count)

#reading the 'whole' file
fhand = open ('mbox-short.txt')
inp = fhand.read()  #reads the whole file into a single string
print(len(inp))  #gives length of the whole file; number of characters
print (inp[:20]) #prints out the characters of a file as a string starting from first till 20th character.

#searchin through a file
fhand = open ('mbox-short.txt')
for line in fhand:
    #line = line.rstrip()
    if line.startswith('From:'): #if the line in fhand starts with From, we print that
        print (line)

#skipping with continue
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() #whitespaces are removed
    if not line.startswith('From:'):  #if the line doesn't starts with From
        continue #goes back to the top of the loop, so all the lines that are uninteresting to us we're going to skip, until we get True.
                 #basically, what continue do is, it skips the lines that there is no From inside, and print 'good' lines with From.
                 #in other words, if it is not a line that contains From, skip it.
    print (line)    
#using 'in' to select lines
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() #whitespaces are removed
    if not 'From:' in line:   #now if line doesn't contain From, in general, we skip it
        continue 
    print(line)
    
    
