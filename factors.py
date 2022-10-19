n,k=list(map(int,(input().split())))
a=[]
for i in range(1,n+1):
    if(n%i==0):
        a.append(i)
if(k<len(a)):
    print(a[k])
else:
    print("1")
