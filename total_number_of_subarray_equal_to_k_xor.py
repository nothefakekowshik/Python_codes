import functools

def xorcheck(alist):
    val=functools.reduce(lambda x, y: x ^ y, alist) 
    return val

def subsetsUtil(A, subset, index):
    
    
    for i in range(index, len(A)):

        subset.append(A[i])

        subsetsUtil(A, subset, i + 1)
        if(xorcheck(subset)==xor_val):
            c+=1

            
        subset.pop(-1)
    print(c)

def subsets(A):

    subset = []
    index = 0
    subsetsUtil(A, subset, index)
        
        

c=0
array = [4,2,2,6,4]

xor_val=6
subsets(array)
