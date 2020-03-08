'''
Created on 2019 M02 21

@author: liux8275
'''
from asgn02 import member_expertise_count
from Connect import Connect

v1 = 1


conn = Connect("dcris.txt")

print("member_id is None (sorted by last name, first name)")
rows = member_expertise_count(conn)
for row in rows:
    print(row)
print("\n")

print("member_id is {}(sorted by last name, first name)".format(v1))
rows = member_expertise_count(conn, member_id=v1)
for row in rows:
    print(row)
    
    
conn.close()