a=[9,7,5,3,1]
b=[0 for i in range(len(a))]
x=2
b[len(a)-1]=a[len(a)-1]
for i in range(len(a)-2,-1,-1):
    b[i]=a[i]+b[i+1]*x
b.reverse()
print(b)