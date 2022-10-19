n=int(input("enter number of elements"))
a=[]
for i in range(n):
    x=int(input("enter values"))
    a.append(x)
for i in range(n):
    for j in range(n-1):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
print("After sorting",*a)