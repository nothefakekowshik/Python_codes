t=int(input())
arr=[]
while t:
    t-=1
    num=int(input())
    fact=1
    for x in range(1,num+1):
        fact=fact*x
    arr.append(fact)
for i in arr:
    print(i)
