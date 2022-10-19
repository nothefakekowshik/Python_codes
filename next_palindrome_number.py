t=int(input())
while t:
	t-=1
	n=int(input())
	for i in range(n+1,1000000+1):
		n+=1
		strn=str(n)
		if(strn==strn[::-1]):
			print(n)
			break
		