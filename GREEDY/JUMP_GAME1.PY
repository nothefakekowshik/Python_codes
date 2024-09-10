'''

For example, if the value of the current square is 3, the player can take either 3 OR 2 OR 1
step in the direction of the last square. The player cannot move in the opposite direction, that is, away from the last square.

'''

from collections import deque

def brute_force_recursive(curr_index,a):
    if curr_index >= len(a)-1:
        return True
    
    max_jump_from_here = min(curr_index + a[curr_index], len(a)-1)
    for next_index in range(curr_index+1, max_jump_from_here+1):
        if brute_force_recursive(next_index,a):
            return True
    return False

def recursive_memo(curr_index, nums,dp):
    if curr_index >= len(nums)-1:
        return True
    
    if dp[curr_index] is not None:
        return dp[curr_index]

    max_jump_from_here = min(curr_index + nums[curr_index], len(nums)-1)
    for next_index in range(curr_index+1, max_jump_from_here+1):
        if recursive_memo(next_index,nums,dp):
            dp[next_index] = True
            return True
        
    dp[curr_index] = False
    return False
    

def iterative_queue(a):
    q = deque([0])
    visited = set()
    visited.add(0)
    while q:
        curr_index = q.popleft()
        if curr_index >= len(a)-1:
            return True    
        max_jump_from_here = min(curr_index + a[curr_index], len(a)-1)
        for next_index in range(curr_index+1,max_jump_from_here+1):
            if next_index not in visited:
                q.append(next_index)
                visited.add(next_index)
    return False
    #for some reason, this solution failed on 156/172 on leetcode.
    
    
def greedy_approach(a):
    max_jump_from_here = 0
    for i in range(len(a)):
        if i > max_jump_from_here:
            return False
        
        max_jump_from_here = max(max_jump_from_here, i+a[i])
        if max_jump_from_here >= len(a)-1:
            return True
        
    return max_jump_from_here >= len(a)-1
        
    

a = [2,3,1,1,4]
# a = [3,2,1,0,4]
dp = [None] * len(a)
print(brute_force_recursive(0,a))
print(recursive_memo(0,a,dp))
print(greedy_approach(a))