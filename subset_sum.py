def subsetsUtil(A, subset, index):
    ans=[]
    for i in range(index, len(A)):

        subset.append(A[i])

        subsetsUtil(A, subset, i + 1)
        if(sum(subset)==summ):
            return True

            
        subset.pop(-1)
    

def subsets(A):

    subset = []
    index = 0
    if(subsetsUtil(A, subset, index)):
        print("true")
    else:
        print("false")
        


array = [-5,10,-3]

summ=30
subsets(array)
