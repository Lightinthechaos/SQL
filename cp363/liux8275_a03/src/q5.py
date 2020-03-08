'''
Created on 2019 M03 8

@author: liux8275
'''
from asgn03 import supp_key_member_count
from Connect import Connect

v1=70

conn = Connect("dcris.txt")

print("supp_key_id is None(sorted by keyword description)")
rows = supp_key_member_count(conn)
for row in rows:
    print(row)
print("\n")

print("supp_key_id is {}(sorted by keyword description)".format(v1))
rows = supp_key_member_count(conn, supp_key_id=v1)
for row in rows:
    print(row)
print("\n")


conn.close()