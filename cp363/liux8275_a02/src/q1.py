'''
Created on 2019 M02 19

@author: liux8275
'''
from asgn02 import publications
from Connect import Connect

v1="Canada"
v2='a'

conn = Connect("dcris.txt")

print("title is None and pub_type_id is None(sorted by last name, first name, title)")
rows = publications(conn)
for row in rows:
    print(row)
print("\n")

print("title is None and pub_type_id is {}(sorted by last name, first name, title)".format(v2))
rows = publications(conn, title=v1)
for row in rows:
    print(row)
print("\n")

print("title is {} and pub_type_id is None(sorted by last name, first name, title)".format(v1))
rows = publications(conn, pub_type_id=v2)
for row in rows:
    print(row)
print("\n")

print("title is {} and pub_type_id is {}(sorted by last name, first name, title)".format(v1,v2))
rows = publications(conn, title=v1, pub_type_id=v2)
for row in rows:
    print(row)
    
    
conn.close()