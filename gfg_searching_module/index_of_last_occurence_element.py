def fetchIndex(a,x):
    low,high=0,len(a)-1
    while(low<=high):
        mid=(low+high)//2
        if(x>a[mid]):
            low=mid+1
        elif(x<a[mid]):
            high=mid-1
        else:
            if(mid==len(a)-1 or a[mid]!=a[mid+1]):
                return mid
            else:
                low=mid+1
    return -1

a=[10,15,20,20,40,40]
x=20
print(fetchIndex(a,x))