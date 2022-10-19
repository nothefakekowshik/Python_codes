n=50
primes=[True for i in range(n+1)]
i=2
while(i*i<=n):
    if(primes[i]==True):
        for j in range(i*i,n+1,i):
            primes[j]=False
    i+=1
for i in range(2,n+1):
    if(primes[i]):
        print(i)
