'''
Created on 2019 M01 28

@author: liux8275
'''
from asgn01 import keyword_table
from Connect import Connect

conn = Connect("dcris.txt")
rows = keyword_table(conn)
print("Keyword is None")
print("Data: ")
for row in rows:
    print(row)

print("\n")
v = 7
rows2 = keyword_table(conn, keyword_id=v)
print("Keyword is 7")
print("Data: ")
for row in rows2:
    print(row)
    
conn.close()
    

