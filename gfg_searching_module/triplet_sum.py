def tripletCheck(a,k):
    a.sort()
    for i in range(0,len(a)-2):
        l=i+1
        h=len(a)-1
        while(l<h):
            if(a[i]+a[l]+a[h]==k):
                return True
            elif(a[i]+a[l]+a[h]>k):
                h-=1
            else:
                l+=1
    return False

a=[1,4,45,6,10,8]
k=22
print(tripletCheck(a,k)) 