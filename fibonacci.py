n=int(input("Enter the length"))
a=0
b=1
arr=[0,1]

for i in range(2,n):
    c=a+b
    a=b
    b=c
    arr.append(c)
print(*arr)
ind=5
print(arr[ind-1])
