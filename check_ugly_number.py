def check(a,b):
    while(a%b==0):
        a=a/b
    return a


n=15
n=check(n,2)
n=check(n,3)
n=check(n,5)
if(n==1):
    print("yes")
else:
    print("no")
