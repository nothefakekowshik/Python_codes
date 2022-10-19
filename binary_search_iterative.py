def binary_search_implementation(a,val):
    low,high=0,len(a)-1
    while(low<=high):
        mid=(low+high)//2
        if(a[mid]==val):
            return True

        elif(a[mid]>val):
            high=mid-1
            
        elif(a[mid]<val):
            low=mid+1
    return False

a=[1,2,4,10,15]
val=1
print(binary_search_implementation(a,val))