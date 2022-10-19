n=9
k=5
a=[]
i=1
a=[0]
while(i<=n):
    a.append(i)
    if(i%k==0):
        for j in range(1,i-1):
            a.append(i+j)
        i=a[i]
    else:
        i+=1
a.remove(0)
print(a)