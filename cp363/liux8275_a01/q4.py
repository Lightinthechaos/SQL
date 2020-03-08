'''
Created on 2019 M01 30

@author: liux8275
'''
from asgn01 import expertise
from Connect import Connect

conn = Connect("dcris.txt")
v1 = 'Arms'
v2 = 'Measures'
print("keyword is None and supp_key is None(sorted by keyword description, supplementary keyword description)")
rows = expertise(conn)
for row in rows:
    print(row)
print("\n")

rows = expertise(conn, keyword=v1)
print("keyword is 'A' and supp_key is None(sorted by keyword description, supplementary keyword description)")
for row in rows:
    print(row)
print("\n")

print("keyword is None and supp_key is 9(sorted by supplementary keyword description, keyword description)")
rows = expertise(conn, supp_key=v2)
for row in rows:
    print(row)
print("\n")

print("keyword is 'A' and supp_key is 9(sorted by keyword description, supplementary keyword description)")
rows = expertise(conn, keyword=v1, supp_key=v2)
for row in rows:
    print(row)
print("\n")

conn.close()
