n = int(input("Enter a number: "))
p = False
i = 2
if (n == 2):
	print(n," is  a prime number")
elif(n>2):
	while(i < n):
		if(n % i == 0):
			P = True
		else:
			p = False
		i = i+1
		
	if(p == True):
		print(n," is  a prime number")
	else:
		print(n, " is not a prime number")
