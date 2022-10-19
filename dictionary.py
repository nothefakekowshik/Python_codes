for _ in range(int(input())) :
    n,k = (int(i) for i in input().split())
    arr = list(map(int,input().strip().split()))
    d=dict.fromkeys(arr,0)
    for i in arr:
        d[i]+=1
    print(d)
    for i in arr:
        if d[i]==k:
            print(i)
            break
    else:
        print(-1)