n=int(input())
arr=[]
c=0
for i in range(n+1):
    arr.append(bin(i).replace("0b",""))
#print(arr)
for i in arr:
    c+=i.count("1")
print(c)
