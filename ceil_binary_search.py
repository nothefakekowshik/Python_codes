a=[1, 2, 8, 10, 10, 12, 19]
x=20
l,r=0,len(a)-1
while(r>l):
    mid=l+(r-l)//2
    if(a[mid]<x):
        l=mid+1
    else:
        r=mid

print("original ")
print(a)
print("dup")
a[r]=x


print(a)

