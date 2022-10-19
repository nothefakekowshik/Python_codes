def firstOcc(a,x):
    low,high=0,len(a)-1
    while(low<=high):
        mid=(low+high)//2
        if(x>a[mid]):
            low=mid+1
        elif(x<a[mid]):
            high=mid-1
        else:
            if(mid==0 or a[mid-1]!=a[mid]):
                return mid
            else:
                high=mid-1
        
    return -1

def lastOcc(a,x):
    low,high=0,len(a)-1
    while(low<=high):
        mid=(low+high)//2
        if(x>a[mid]):
            low=mid+1
        elif(x<a[mid]):
            high=mid-1
        else:
            if(mid==len(a)-1 or a[mid+1]!=a[mid]):
                return mid
            else:
                low=mid+1
    return -1


def countOcc(a,x):
    firstOcc_val=firstOcc(a,x)
    
    lastOcc_val=lastOcc(a,x)
    if(firstOcc_val==-1):
        print("0")
    
    else:
        print(lastOcc_val-firstOcc_val+1)


# a=[10,10,10,10,10]
# x=10




# a=[10,20,20,20,30,30]
# x=20        

a=[0,0,0]
x=1

countOcc(a,x)


