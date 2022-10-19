#o/p: 0,0,0,0,0,0,1,1,1,1,1,1,1

a=[0,0,1,0,1,1,0,0,0,1,1,1,1]
curr_ind=0
for i in range(len(a)):
    if(a[i]==0):
        a[curr_ind],a[i]=a[i],a[curr_ind]
        curr_ind+=1
print(a)