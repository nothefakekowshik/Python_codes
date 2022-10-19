t=int(input())
while t:
    t-=1
    a,b,c=list(map(str,input().split()))
    c=int(c)
    while True:
        temp=a+b
        a=b
        b=temp
        if(len(temp)>=c):
            break

    print(temp[c-1])
