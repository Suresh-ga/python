upper=10
 
lower=4

for x in range(lower,upper+1):
	sum=0
	z=x
	
	for i in range(1,x):
		y=x%i
		if(y==0):
			sum+=i
		
	if(z==sum):
		print(sum)
			
	else:
		print("not perfect")

	