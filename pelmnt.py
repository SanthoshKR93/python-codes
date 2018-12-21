import requests,bs4
#requests module is only needed if we are downloading the data from internet
file1=open('myfile.html')
bs4obj=bs4.BeautifulSoup(file1,"lxml")
pelement=bs4obj.select('p')
c=len(pelement)
print(c)
i=0
while i<c:
   print(str(pelement[i]))
   print(pelement[i].getText())
   print(pelement[i].attrs)
   i=i+1
file1.close()
