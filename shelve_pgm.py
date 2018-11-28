import shelve
sfile=shelve.open('dbshelve')
var={'name':'san','age':'25','status':'unemployed'}
sfile['variable']=var
print(list(sfile.keys()))
print(list(sfile.values()))
sfile.close()
