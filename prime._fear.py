n=30
prime=[True for i in range(n+1)]
i=2
c=0
while(i*i<=n):
    if(prime[i]==True):
        for j in range(i*i,n+1,i):
            prime[j]=False
    i+=1
prime_val=[]
for i in range(2,n+1):
    if(prime[i]==True):
        prime_val.append(str(i))
print(prime_val)
c=0
fear_list=[]
for i in prime_val:
    prime_list=[j for j in i]
    for k in prime_list:
        res=all(z in k for z in prime_val)
        if(res):
            c+=1
            print(c) 

    # print(*prime_list)
    # prime_list.clear()

