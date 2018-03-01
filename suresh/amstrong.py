a=int(input("enter the number"))
print(a)
s=a
sum=0
while(a>0):
	b=a%10
	sum=sum+(b*b*b)
	a=a//10

if(sum==s):
	print(" given no is amstrong")
	
else:
	print("not amstrong")
	