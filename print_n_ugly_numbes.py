def maxDivide(a,b):
    while(a%b==0)        :
        a=a//b
    return a
def isUgly(no):
    no=maxDivide(no,2)
    no=maxDivide(no,3)
    no=maxDivide(no,5)
    if(no==1):
        return 1
    else:
        return 0

a=[]
n=10
c=1
i=1
while(n>c):
    i+=1
    if(isUgly(i)):
        a.append(i)
        c+=1    

for i in a:
    print(i,end=" ")
    




