def collatz(number):
 if number%2==0:
  return(number//2)
 elif number%2==1:
  return(3*number+1)
print('enter the number:')
number=int(input())
n=1
while n>=1: 
 n=collatz(number)
 print(n)
 number=int(n)
 if n==1:
  break
