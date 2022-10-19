a=100
low,high=1,a
while(low<=high):
    mid=(low+high)/2
    if(mid*mid==a):
        print("mid")
        break
    elif(mid*mid>a):
        high=mid-1
    else:
        low=mid+1
        ans=mid

print(int(ans+1))
