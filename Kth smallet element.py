n=int(input('how many elements'))
a=[]
for i in range(n):
    x=int(input('enter the element'))
    a.append(x)
a.sort()
print(a)
k=int(input('Which element?'))
print(a[k-1])

