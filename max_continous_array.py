n=10
# a=[18,-33,31,33,30,-14,32,30,16,17]
# a=[21,-22,-22,5,-31,-24,5,-23]
a=[6,3,8,5,2,5]
a.sort()
for i in range(len(a)):
    if(a[i]<0):
        a[i]=a[i]*-1

a=set(a)
a=list(a)

print(a)
max_index=0
ele=0
for i in range(len(a)):
    c=0
    for j in range(i,len(a)-1):
        if(a[j+1]-a[j]==1):
            c+=1
    if(max_index<c):
        max_index=c
        ele=a[j]
print(max_index)
# print(ele)

