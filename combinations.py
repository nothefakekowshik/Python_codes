from itertools import combinations
c=0
print("Enter the array elements")
arr=list(map(int,input().split()))
comb=list(combinations(arr,2))
su=int(input("Enter the sum value"))
print(comb)
for i in comb:
    if(sum(i)==su):
        c+=1
print(c)