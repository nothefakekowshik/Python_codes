a=[5,8,6,13,3,-1]
k=16
prefix_sum=0
set_a=set()
flag=0
for i in a:
    if(prefix_sum==k):
        flag=1
        break
    prefix_sum+=i
    if(prefix_sum-k in set_a):
        flag=1
        break
    set_a.add(prefix_sum)
if(flag==1):
    print("Found")
else:
    print("No")