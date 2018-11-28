n=100
a=0
b=0
d=0
list=[]
print('enter the divisor')
a=int(input())
print('enter the remainder')
b=int(input())
print('enter the common difference')
d=int(input())
print('enter the first number')
a=int(input())
while n<1000:
    if (n%a)==b and (n-a)%d==0:
       list.append(n)
       #print(n)
    n=n+1
print(max(list))
print(min(list))    
