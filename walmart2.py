n=int(input())
production_time=list(map(int,input().split()))
polish_time=list(map(int,input().split()))
dict_array={}

perm_min=10**6
perm_val=10**6

if(production_time==polish_time):
    ans=sum(production_time)+production_time[0]
    print(ans)
else:
    for i in range(n):
        curr_sub=production_time[i]-polish_time[i]
        if(curr_sub>=0):
            



            

print(dict_array)
            