import math
print("Enter the values")
a=list(map(int,input().split()))
length=len(a)
#print("length of the array is"+str(length))
product=1
seven=7
#print("index is "+str(ind))
if(a[length-1]==7):
    print("-1")
else:
    if seven in a:
        ind=a.index(7)
        a=a[ind+1:]
        print(math.prod(a))
    else:
        for i in range(length):
            if(i!=7):
                product=product*a[i]
        print(product)
