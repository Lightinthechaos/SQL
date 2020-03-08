'''
Created on 2019 M04 1

@author: liux8275
'''
from Connect import Connect
from asgn04 import constraint_info

conn = Connect("dcris.txt")
table_schema = "dcris"
v1 = "FOREIGN KEY"


print("table_schema is {} and constraint_type is None".format(table_schema))
rows = constraint_info(conn, table_schema)
for row in rows:
    print(row)
print("\n")

print("table_schema is {} and constraint_type is {}".format(table_schema, v1))
rows = constraint_info(conn, table_schema, constraint_type=v1)
for row in rows:
    print(row)
print("\n")