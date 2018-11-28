import os
list1=['test1.py','test2.py','test3.py','test4.py']
for filenames in list1:
   abc=str(os.path.join('home/killbox',filenames))
   print(abc)
