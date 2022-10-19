def merge(a):
    if(len(a)>1):
        mid=len(a)//2
        left_side=a[:mid]
        right_side=a[mid:]
        merge(left_side)
        merge(right_side)
        i,j,k=0,0,0
        while(i<len(left_side ) and j<len(right_side)):
            if(left_side[i]<right_side[j]):
                a[k]=left_side[i]
                i+=1
                k+=1
            else:
                a[k]=right_side[j]
                j+=1
                k+=1
        while(i<len(left_side)):
            a[k]=left_side[i]
            k+=1
            i+=1
        while(j<len(right_side)):
            a[k]=right_side[j]
            k+=1
            j+=1
            


a = [12, 11, 13, 5, 6, 7]

print(a)
merge(a)
print()
print(a)