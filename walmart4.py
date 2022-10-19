t=int(input())
while t:
    t-=1
    a,b=list(map(int,input().split()))
    days_array=[]
    windays_array=[]
    for i in range(a):
        days,win_days=list(map(int,input().split()))
        days_array.append(days)
        windays_array.append(win_days)
    print(days_array)
    print(windays_array)
        

