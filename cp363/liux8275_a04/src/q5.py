'''
Created on 2019 M04 1

@author: liux8275
'''
from Connect import Connect
from asgn04 import key_info

conn = Connect("dcris.txt")
constraint_schema = "dcris"
v1 = "pub"
v2 = "pub_type"


print("constraint_type is {} and table_name is None and ref_table_name is None".format(constraint_schema))
rows = key_info(conn, constraint_schema)
for row in rows:
    print(row)
print("\n")

print("constraint_type is {} and table_name is {} and ref_table_name is None".format(constraint_schema, v1))
rows = key_info(conn, constraint_schema, table_name=v1)
for row in rows:
    print(row)
print("\n")

print("constraint_type is {} and table_name is None and ref_table_name is {}".format(constraint_schema, v2))
rows = key_info(conn, constraint_schema, ref_table_name=v2)
for row in rows:
    print(row)
print("\n")

print("constraint_type is {} and table_name is {} and ref_table_name is {}".format(constraint_schema, v1, v2))
rows = key_info(conn, constraint_schema, table_name=v1, ref_table_name=v2)
for row in rows:
    print(row)
print("\n")