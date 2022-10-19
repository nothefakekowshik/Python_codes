a=[7,10,4,3,6,5,2]
#o/p: 10 6 5 2
for i in range(len(a)):
    flag=0
    for j in range(i+1,len(a)):
        if(a[i]<=a[j]):
            flag=1
            break
    if(flag==0):
        print(a[i],end=" ")
