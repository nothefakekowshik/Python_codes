from itertools import combinations
n=int(input("How many elements?"))
arr=list(map(int,input().split()))
comb=list(combinations(arr,2))
#su=int(input("Enter the value of sum"))
suma=[]
for i in comb:
    suma=sum(i)
