flag=0
summ=int(input("Enter the sum value"))
print("Enter the array values")
a=list(map(int,input().split()))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        for k in range(j+1,len(a)):
            if(a[i]+a[j]+a[k]==summ):
                flag=1
                print("triplet found")
                print(a[i])
                print(a[j])
                print(a[k])
                break
if(flag==0):
    print("No triplet")
    
