'''
Created on 2019 M03 8

@author: liux8275
'''
from asgn03 import keyword_count
from Connect import Connect

v1=7

conn = Connect("dcris.txt")

print("keyword_id is None(sorted by keyword description)")
rows = keyword_count(conn)
for row in rows:
    print(row)
print("\n")

print("keyword_id is {}(sorted by keyword description)".format(v1))
rows = keyword_count(conn, keyword_id=v1)
for row in rows:
    print(row)
print("\n")


conn.close()