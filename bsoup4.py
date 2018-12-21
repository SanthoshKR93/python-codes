import requests,bs4
file1=open('myfile.html')
bs4object=bs4.BeautifulSoup(file1,"lxml")
elem=bs4object.select('#author')
print(len(elem))
print(str(elem))
elem[0].getText()
print(elem[0].attrs)
file1.close()
