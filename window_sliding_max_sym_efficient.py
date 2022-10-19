a=[1,8,30,-5,20]
k=3
curr_sum=sum(a[:k])
print(curr_sum)
for i in range(k,len(a)):
    curr_sum=curr_sum+a[i]-a[i-k]
    print(curr_sum)
