from typing import DefaultDict


a=[1,3,4,5,7]
b=[2,3,5,6]
dict={}
for i in a:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
for i in b:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
        
for i,j in dict.items():
    if(j==2):
        print(i,end=" ")
print()