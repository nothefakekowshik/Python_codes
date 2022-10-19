def binary_search(a,k,mid,low,high):
    if(high>=low):
        if(a[mid]==k):
            return True
        elif(a[mid]>k):
            low=0
            high=mid-1
            mid=(low+high)//2
            return binary_search(a,k,mid,low,high)
        else:
            low=mid+1
            high=len(a)-1
            mid=(low+high)//2
            return binary_search(a,k,mid,low,high)
    else:
        return False
    
a=[5,2,1,8,6]
a.sort()
k=10
mid=len(a)//2
print(binary_search(a,k,mid,0,len(a)-1))