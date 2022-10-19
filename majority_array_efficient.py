from typing import Counter


a=[8,3,4,8,8,3]
ind=0
temp_count=0
for i in range(len(a)):
    if(a[ind]==a[i]):
        temp_count+=1
    else:
        temp_count-=1
    if(temp_count==0):
        ind=i
        temp_count=1
perm_counter=0
for i in range(len(a)):
    if(a[ind]==a[i]):
        perm_counter+=1
if(perm_counter>len(a)//2):
    print(a[ind])
else:
    print("-1")
