t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    for i in a:
        if(i==a[0]):
            flag=1
        else:
            flag=0
    if(flag==1):
        print("NO")
    else:
        print("YES")
    t-=1