import os
for root, dirs, files in os.walk("D:\\fsearch_oop\\test_folder", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))