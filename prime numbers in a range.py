print("Enter the numbers")
first,last=list(map(int,input().split()))
for i in range(first,last+1):
    k=0
    for j in range(1,last+1):
        if(i%j==0):
            k+=1
    if(k==2):
        print(i,end=" ")

