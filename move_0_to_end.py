#o/p:1, 2, 4, 3, 5, 0, 0

a=[1, 2, 0, 4, 3, 0, 5, 0]
curr_ind=0
for i in range(len(a)):
    if(a[i]!=0):
        a[curr_ind],a[i]=a[i],a[curr_ind]
        curr_ind+=1
print(a)
