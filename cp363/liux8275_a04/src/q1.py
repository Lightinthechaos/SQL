'''
Created on 2019 M03 14

@author: liux8275
'''
from Connect import Connect
from asgn04 import table_info

conn = Connect("dcris.txt")
table_schema = "dcris"
v1 = "keyword"

print("table_schema is {} and table_name is None".format(table_schema))
rows = table_info(conn, table_schema)
for row in rows:
    print(row)
print("\n")

print("table_schema is {} and table_name is {}".format(table_schema, v1))
rows = table_info(conn, table_schema, table_name=v1)
for row in rows:
    print(row)
print("\n")

