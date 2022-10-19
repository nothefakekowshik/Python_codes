def partition(a,low,high):
    pivot_ind=low
    pivot_ele=a[pivot_ind]

    while(low<high):
        while low<len(a) and a[low]<=pivot_ele:
            low+=1
        while(a[high]>pivot_ele):
            high-=1
        if(low<high):
            a[low],a[high]=a[high],a[low]
    a[pivot_ind],a[high]=a[high],a[pivot_ind]
    return high

def qsort(a,start,end):
    if(start<end):
        p=partition(a,start,end)
        qsort(a,start,p-1)
        qsort(a,p+1,end)



a=[10,5,1,8,3,6]
qsort(a,0,len(a)-1)
print(a)