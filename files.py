# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 16:34:55 2021

@author: mehdiyeva
"""
"""7.1 Write a program that prompts for a file name, then opens that file and reads through the file, 
and print the contents of the file in upper case. Use the file words.txt to produce the output below."""
#If the file IS relativelyy small:
fname = input("Enter file name: ") # Use words.txt as the file name
try:
    fh = open(fname) #we are trying to open while and check if it exists.
    
except:
    
    print ('Please check the file name again:', fname) # if it does not exist, ask user to change the file name.
    quit()
    
inp = fh.read() #if the file name user entered exists, then we read the file into a single string.
for line in fh:   
    line = line.rstrip()
print (inp.upper())
print (len(inp))

#If the file is NOT relativelyy small (usually it is better to use this one if we do not have any info. about the size of the file):
fname = input("Enter file name: ")   
try:
    fh = open(fname) #open does not read the file, it kind of gives us this little portal where we can take a look at the file. It just is a file handle. To read a file we are going to write a for loop. 
except:
    print('Cannot open the file ',fname ,'please try again')
    quit()

for line in fh:
    
    line = line.rstrip().upper() #we used two methods simultaneously: rstip & upper. 
    print(line)
    
"""7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
    X-DSPAM-Confidence:    0.8475
    Count these lines and extract the floating point values from each of the lines 
    and compute the average of those values and produce an output as shown below. 
    Do not use the sum() function or a variable named sum in your solution."""

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0  #always start counting from zero
total = 0  #always start summing from zero
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): #we are looking for a special file
        continue
    count = count + 1
    #print(line)
#print("Number of lines with X-DSPAM-Confidence: ", count)
    f = line.find (':') #find the position of ':'
    extrValues = line[f+1:] #extracting those values
    #print(extrValues)
    total = total + float(extrValues) #finding the sum of floating values so that we can later find the average (ceminin sayina nisbeti=average). That's why we're summing all.
    avr = total/count   
    #print(line)
print("Average spam confidence:", avr)


