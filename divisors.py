import math 
def divisors(n) : 
	c=0
	for i in range(1,(int)(math.sqrt(n))+1) : 
		if (n%i==0) : 
			if (n/i==i) : 
				c=c+1
			else : 
				c=c+2
	return c
t=int(input())
while t:
    t-=1
    n=int(input())
    if(divisors(n)%2==1):
        print("1")
    else:
        print("0")
        

