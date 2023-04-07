import findmyfile
import time

t1 = time.time()
database = findmyfile.FilesDB("D:\\fsearch_oop\\excel_test")
t2 = time.time()
print("Time to create database: ", t2-t1)
matches = database.get_matching_files("Sanjin")
t3 = time.time()
print("Time to search database: ", t3-t2)
for match in matches:
    print(match)