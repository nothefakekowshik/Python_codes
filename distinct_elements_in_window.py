from typing import DefaultDict


n,k=10,4
a=[1,2,2,1,3,1,1,3]
dict=DefaultDict(lambda:0)

distinct_elements=0

for i in range(0,k):
    if(dict[a[i]]==0):
        distinct_elements+=1
    dict[a[i]]+=1

print(distinct_elements)

for i in range(k,len(a)):
    if(dict[a[i-k]]==1):
        distinct_elements-=1
    dict[a[i-k]]-=1
    if(dict[a[i]]==0):
        distinct_elements+=1    
    dict[a[i]]+=1
    print(distinct_elements)