'''
Created on 2019 M02 19

@author: liux8275
'''
from asgn02 import pub_counts
from Connect import Connect

v1 = 1
v2 = 'a'

conn = Connect("dcris.txt")

print("member_id is {} and pub_type_id is None(sorted by last name, first name, title)".format(v1))
rows = pub_counts(conn, member_id=v1)
for row in rows:
    print(row)
print("\n")

print("member_id is {} and pub_type_id is {}(sorted by last name, first name, title)".format(v1,v2))
rows = pub_counts(conn, member_id=v1, pub_type_id=v2)
for row in rows:
    print(row)
    
    
conn.close()