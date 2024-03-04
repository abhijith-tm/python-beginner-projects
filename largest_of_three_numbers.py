a = int(input("Enter First Number: "))
b = int(input("Enter second Number: "))
c = int(input("Enter Third Number: "))

if(a>b & a>c):
    print(a," is largest")
  
elif(b>a & c<b):
    print(b,"is largest")
   
else:
    print(c," is largest")
    
