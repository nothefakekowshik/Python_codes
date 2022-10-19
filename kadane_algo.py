a = [-2, -3, 4, -1, -2, 1, 5, -3]
temp_sum,perm_sum=0,a[0]
temp_start,perm_start,perm_end=0,0,0
for i in range(len(a)):
    temp_sum+=a[i]
    if(temp_sum<0):
        temp_sum=0
        temp_start=i+1
    elif(temp_sum>perm_sum):
        perm_sum=temp_sum
        perm_start=temp_start
        perm_end=i
        
print(perm_sum)
print(perm_start)
print(perm_end)