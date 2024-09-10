def min_jumps_recursive(arr, start, n):
    # Base case: If we've reached the last element
    if start >= n - 1:
        return 0
    
    # If the current element is 0, we can't move further
    if arr[start] == 0:
        return float('inf')
    
    # Initialize the minimum jumps required as infinity
    min_jumps = float('inf')
    
    # Try all possible jumps from the current position
    for i in range(1, arr[start] + 1):
        # Recursively calculate the minimum jumps needed from the new position
        jumps = min_jumps_recursive(arr, start + i, n)
        
        # If this jump results in reaching the end, update the minimum jumps
        if jumps != float('inf'):
            min_jumps = min(min_jumps, jumps + 1)
    
    return min_jumps

def min_jumps_memo(arr, start, n, dp):
    # Base case: If we've reached the last element
    if start >= n - 1:
        return 0
    
    # If the current element is 0, we can't move further
    if arr[start] == 0:
        return float('inf')
    
    # If this subproblem has already been solved, return the stored result
    if dp[start] != -1:
        return dp[start]
    
    # Initialize the minimum jumps required as infinity
    min_jumps = float('inf')
    
    # Try all possible jumps from the current position
    for i in range(1, arr[start] + 1):
        # Recursively calculate the minimum jumps needed from the new position
        jumps = min_jumps_memo(arr, start + i, n, dp)
        
        # If this jump results in reaching the end, update the minimum jumps
        if jumps != float('inf'):
            min_jumps = min(min_jumps, jumps + 1)
    
    # Store the result in the memoization array before returning
    dp[start] = min_jumps
    return dp[start] 

    # n ** 2 solution
    


def greedy(a):
    if a[0] == 0:
        return -1
        
    near = far = jumps = 0

    while far < len(a) - 1:
        farthest = 0
        for i in range(near, far + 1):
            farthest = max(farthest, i + a[i])
        
        if farthest == 0:
            return -1
            
        near = far + 1
        far = farthest
        jumps += 1
    
    return jumps
        
        
    

arr = [2,3,1,1,4]
print(min_jumps_recursive(arr, 0, len(arr)))
dp=[-1] * 5
print(min_jumps_memo(arr,0,5,dp))
print(greedy(arr))