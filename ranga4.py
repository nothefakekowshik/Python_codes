t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    l=len(a)
    print(a[l-1]-a[0])
    t-=1