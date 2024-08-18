# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 14:40:36 2021

@author: mehdiyeva
"""

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur =conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts (email TEXT, 
            count INTEGER)''')

fname = input('Enter the file name: ')
if (len(fname) < 1): 
    fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    #let's do some database
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,)) # '?' is a placeholder
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                    VALUES (?, 1)''', (email, ))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email, ))
    conn.commit()
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    



    

    
