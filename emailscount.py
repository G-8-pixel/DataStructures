# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 01:37:06 2021

@author: mehdiyeva
"""

import sqlite3
conn = sqlite3.connect('emailcount.sqlite')
cur =conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts (org TEXT, 
            count INTEGER)''')

fname = input ('Enter name: ')
if len(fname)<1:
    fname = 'mbox.txt'
fh = open(fname)
# print(fh)
for line in fh:
    line = line.rstrip()
    if not line.startswith('From: '): 
        continue
    words = line.split()
    email = words[1] 
    org = email.split('@')[1] # split emails from the specific character @ and get only domains
    # print(org)      
    # print(org[1])
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,)) # '?' is a placeholder
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, 1)''', (org, ))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org, ))
    conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    