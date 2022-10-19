
import sys 
A = [40,10,20,10] 
ind=[]
for i in range(len(A)): 
	
	
	min_idx = i 
	for j in range(i+1, len(A)): 
		if A[min_idx] > A[j]: 
			min_idx = j 
			
	val=A[min_idx]
	ind.append(A.index(val))
	A[i], A[min_idx] = A[min_idx], A[i] 

print ("Sorted array") 
for i in range(len(A)): 
	print("%d" %A[i],end=" ")
print()
print(ind)
