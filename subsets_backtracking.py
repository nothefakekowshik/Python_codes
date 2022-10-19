
def subsetsUtil(A, subset, index): 
	print(*subset) 
	for i in range(index, len(A)): 
		
		
		subset.append(A[i]) 	
		
		
		subsetsUtil(A, subset, i + 1) 
		
		
		subset.pop(-1) 
	return
def subsets(A): 
	
	subset = [] 
	
	
	index = 0
	subsetsUtil(A, subset, index) 
	

array = [2,6,9,15] 


subsets(array) 


