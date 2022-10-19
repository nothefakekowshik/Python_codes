def merge(a):
    if(len(a)>1):
        mid=len(a)//2
        left_part=a[:mid]
        right_part=a[mid:]
        merge(left_part)
        merge(right_part)
        i,j,k=0,0,0
        while(i<len(left_part) and j<len(right_part)):
            if(left_part[i]<right_part[j]):
                a[k]=left_part[i]
                i+=1
                k+=1
            else:
                a[k]=right_part[j]
                j+=1
                k+=1
        while(i<len(left_part)):
            a[k]=left_part[i]
            k+=1
            i+=1
        while(j<len(right_part)):
            a[k]=right_part[j]
            k+=1
            j+=1
            

a=[10,4,0,6,7,1,2]
merge(a)
print(a)