'''
Created on 2019 M01 30

@author: liux8275
'''
from asgn01 import pub_table
from Connect import Connect

conn = Connect("dcris.txt")

v1 = 35
v2 = 'p'
print("pub type id is None and member id is None:")
rows1 = pub_table(conn)
for row in rows1:
    print(row)
print("\n")   
print("pub type id is None:")
rows2 = pub_table(conn, member_id=v1)
for row in rows2:
    print(row)
print("\n")
print("member id is None:")    
rows3 = pub_table(conn, pub_type_id=v2)
for row in rows3:
    print(row)
print("\n")
print("pub type id is None and member id is None:")   
rows4 = pub_table(conn, member_id=v1, pub_type_id=v2)
for row in rows4:
    print(row)
    
conn.close()