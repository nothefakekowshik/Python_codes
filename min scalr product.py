n=int(input())
sum=0
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
a1.sort()
a2.sort(reverse=True)
print(a1)
print(a2)
for i in range(n):
    sum+=(a1[i]*a2[i])
print(sum)