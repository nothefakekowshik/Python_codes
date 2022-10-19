t=int(input())
while t:
    t-=1
    n,b=list(map(int,input().split()))
    a=list(map(int,input().split()))
    a.sort()
    summ=0
    c=0
    for i in a:
        if(summ+i<=b):
            summ+=i
            c+=1
    print(c)
    