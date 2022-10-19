a,b=2,4
n=b

prime=[True for i in range(n+1)]
i=2
while(i*i<=n):
    if(prime[i]==True):
        for j in range(i*i,n+1,i):
            prime[j]=False
    i+=1
prime_val=[]
for i in range(2,n+1):
    if(prime[i]==True ):
        prime_val.append(i)
prime_real_val=[]
for i in prime_val:
    if(i>=a and i<=b):
        prime_real_val.append(i)
print(len(prime_real_val))
