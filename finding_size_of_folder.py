import os
path='/home/killbox/python/'
total=0
dirr=os.listdir(path)
for files in dirr:
   fil=os.path.join(path,files)
   total=total+os.path.getsize(fil)
print(str(total) +" "+"bytes")
