'''
Created on 2019 M03 8

@author: liux8275
'''
from asgn03 import expertise_count
from Connect import Connect

v1=90

conn = Connect("dcris.txt")

print("member_id is None(sorted by last name, first name)")
rows = expertise_count(conn)
for row in rows:
    print(row)
print("\n")

print("member_id is {}(sorted by last name, first name)".format(v1))
rows = expertise_count(conn, member_id=v1)
for row in rows:
    print(row)
print("\n")


conn.close()