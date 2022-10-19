t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    k=int(input())
    for i in range(0,len(a)+1):
        if(a[i]<a[i+1]):
            continue
        else:
            print(a[i],end=" ")
    t-=1