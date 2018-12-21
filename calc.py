flag=1
while flag==1:
   print("""Type in the operation
   add for addition
   sub for subtraction
   mul for multiplication
   div for division
   mod for modulus
   quo for quotient
   exp for exponentiation""")
   opt=str(raw_input())
   print("Enter the First value")
   val1=int(input())
   print("Enter the Second value")
   val2=int(input())
   if opt=='add':
      sum=val1+val2
      print("sum is"+" "+str(sum))
   elif opt=='sub':
      dif=val1-val2
      print("difference is"+" "+str(dif))
   elif opt=='mul':
      prod=val1*val2
      print("product is"+" "+str(prod))
   elif opt=='div':
      divd=val1/val2
      print("result is"+" "+str(divd))
   elif opt=='mod':
      rem=val1%val2
      print("remainder is"+" "+str(rem))
   elif opt=='quo':
      quot=val1//val2
      print("quotient is"+" "+str(quot))
   elif opt=='exp':
      expo=val1**val2
      print("result is"+" "+str(expo))
   else:
      print("wrong choice")
   
   print("Do you want to continue y or n")
   choice=str(raw_input())
   if str(choice)=='y':
      flag=1 
   elif str(choice)=='n':
      flag=0
