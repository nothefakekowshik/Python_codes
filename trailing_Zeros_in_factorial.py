n=60
a=[]
while(n%5==0):
    a.append(n//5)
    n=n//5

print(sum(a))