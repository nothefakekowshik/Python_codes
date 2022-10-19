from collections import deque
def printMax(arr, n, k):
	dq = deque()
	for i in range(k):
		while dq and arr[i] >= arr[dq[-1]] :
			dq.pop()
		dq.append(i)
	for i in range(k, n):
		print(str(arr[dq[0]]) + " ", end = "")
		while dq and dq[0] <= i-k:
			dq.popleft()
		while dq and arr[i] >= arr[dq[-1]] :
			dq.pop()
		dq.append(i)
	print(str(arr[dq[0]]))
	
if __name__=="__main__":
	arr = [12, 1, 78, 90, 57, 89, 56]
	k = 3
	printMax(arr, len(arr), k)
	

