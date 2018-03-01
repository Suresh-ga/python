upper=200
 
lower=150

for x in range(lower,upper+1):
	sum=0
	z=x
	while(x>=1):
		y=x%10
		sum+=(y**3)
		x=x//10
		if(z==sum):
			print(sum)
			
		else:
			print("not armstrong")

	
