import os
import time
import datetime
file1=raw_input("enter the file name")
file2=os.getcwd()
stri=os.path.join(file2,file1)
max_time = int(raw_input('Enter the amount of seconds you want to run this: '))
start_time = time.time()
while (time.time() - start_time) < max_time:
   file4=open(stri,'r+a+')
   t=str(datetime.datetime.now().replace(microsecond=0).isoformat())
   file4.write(t)
   file4.write("\n")
file4.close()

