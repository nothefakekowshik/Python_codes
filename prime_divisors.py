import math
n=35
for i in range(1,int(math.sqrt(n))+1):
    if(n%i==0):
        print(i,end=" ")
temp_val=i
for i in range(temp_val,0,-1):
    if(n%i==0):
        print(n//i,end=" ")
print()

for i in range(1,int(math.sqrt(n))+1):
    if(n%i==0):
        print(i,end=" ")
        if(i!=n//i):
            print(n//i,end=" ")