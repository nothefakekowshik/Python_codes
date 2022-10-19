t=int(input())
while t:
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    for i in range(len(a)):
        a[i]=(a[i]-k)

    print(a)
    t-=1