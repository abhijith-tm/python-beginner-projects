n = int(input("Enter a number: "))
sum = 0
reverse = 0
while(n>0):
	d = n%10
	n = int(n/10)
	reverse = reverse+d*10

print(reverse)
	
