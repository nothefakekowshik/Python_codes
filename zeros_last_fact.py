import math
n=100
fact=math.factorial(n)
fact=str(fact)
fact=fact[::-1]
c=0
for i in fact:
    if(i=="0"):
        c+=1
    else:
        break
print(c)
    
    