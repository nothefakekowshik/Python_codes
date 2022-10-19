n=15
k=4
i=1
a=[0]
while(i<=10):
    a.append(i)
    if(a.index(i)%k==0):
        a.append(i)
        i+=1
        
    else:
        i+=1

a.remove(0)
print(a)
print(len(a))