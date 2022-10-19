def findPeak(a):
    low,high=0,len(a)-1
    while(low<=high):
        mid=(low+high)//2
        if (mid==0 or a[mid-1]<=a[mid]) and (mid==len(a)-1 or a[mid+1]<=a[mid]):
            return mid
        if(mid>0 and a[mid-1]>=a[mid]):
            high=mid-1
        else:
            low=mid+1
    return -1

a=[120,80,40]
val=findPeak(a)
print(a[val])
#o/p: 20







'''a=[10,20,15,5,23,90,60]
o/p:20 or 90

a=[80,70,60]
o/p: 80

linear search : o(n)

'''