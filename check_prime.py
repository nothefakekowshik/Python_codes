import math
def check_prime(n):
    if(n<1):
        return False
    if(n==1):
        return False
    if(n==2 or n==3):
        return True
    if(n%2==0 or n%3==0 or n%4==0):
        return False
    else:
        for i in range(5,int(math.sqrt(n)),6):
            if(n%i==0 or n%(i+2)==0):
                return False
    return True
    

for i in range(1,20):
    print(i,check_prime(i),end=" ")