def partition(a,low,high):
    pivot_ele=a[low]
    pivot_ind=low
    while(low<high):
        while(low<len(a) and a[low]<=pivot_ele):
            low+=1
        while(a[high]>pivot_ele):
            high-=1
        if(low<high):
            a[low],a[high]=a[high],a[low]
    a[pivot_ind],a[high]=a[high],a[pivot_ind]
    return high
        

def quicksort(a,low,high):
    if(low<high):
        end=partition(a,low,high)
        quicksort(a,low,end-1)
        quicksort(a,end+1,high)

        

a=[10,5,1,8,3,6]
quicksort(a,0,len(a)-1)
print(a)