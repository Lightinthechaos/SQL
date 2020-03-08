'''
Created on 2019 M01 30

@author: liux8275
'''
from asgn01 import member_expertise
from Connect import Connect

v1=1
v2=7
conn = Connect("dcris.txt")
print("keyword_id is None and member_id is None")
rows = member_expertise(conn)
for row in rows:
    print(row)
print("\n")

print("keyword_id is None and member_id is 1(sorted by last name, first name, keyword description)")
rows = member_expertise(conn, member_id=v1)
for row in rows:
    print(row)
print("\n")

print("keyword_id is 7 and member_id is None(sorted by last name, first name, keyword description)")
rows = member_expertise(conn, keyword_id=v2)
for row in rows:
    print(row)
print("\n")

print("keyword_id is 7 and member_id is 1(unsorted by keyword description, last name, first name)")
rows = member_expertise(conn, member_id=v1, keyword_id=v2)
for row in rows:
    print(row)
    
conn.close()