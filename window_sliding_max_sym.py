a=[1,8,30,-5,20]
k=3
perm_sum=0
for i in range(0,len(a)-k+1):
    temp_sum=0
    for j in range(0,k):
        temp_sum+=a[i+j]

    perm_sum=max(temp_sum,perm_sum)
print(perm_sum)


    
