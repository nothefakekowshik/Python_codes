#code
from itertools import permutations
t=int(input())
while t:
    n=input()
    p=permutations(list(n))
    for i in p:
        x=int(''.join(i))
        if(x%8==0):
            print("Yes")
            break
    else:
            print("No")
    t-=1