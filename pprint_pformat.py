import pprint
file1=[{'name':'san','age':'25','string':'hello'},{'name':'athul','age':'25','string':'world'}]
pprint.pformat(file1)
file2=open('xx.py','w+')
file2.write(pprint.pformat(file1))
file2.close()
