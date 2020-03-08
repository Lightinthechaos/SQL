'''
Created on 2019 M02 21

@author: liux8275
'''
from asgn02 import all_expertise
from Connect import Connect

v1 = 1


conn = Connect("dcris.txt")

print("member_id is None (sorted by last name, first name, keyword description, supplementary keyword description)")
rows = all_expertise(conn)
for row in rows:
    print(row)
print("\n")

print("member_id is {}(sorted by last name, first name, keyword description, supplementary keyword description)".format(v1))
rows = all_expertise(conn, member_id=v1)
for row in rows:
    print(row)
    
    
conn.close()