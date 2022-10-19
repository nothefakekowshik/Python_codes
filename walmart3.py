n=int(input())
a=[0 for i in range(n)]
s=[0 for i in range(2**10)]

queries=int(input())
for _ in range(queries):
    l,r=list(map(int,input().split()))
    j=1
    for i in range(l-1,r):
        a[i]=a[i]+j
        j+=1


print(a)
