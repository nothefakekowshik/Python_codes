'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

'''

def solve_with_brute_force(a):
    prod = [1] * len(a)
    for i in range(len(a)):
        curr_val = 1
        for j in range(0,i):
            curr_val *= a[j]
        for k in range(i+1,len(a)):
            curr_val *= a[k]
        prod[i] = curr_val
    print(prod)
    
def solve_with_optimized(a):
    n = len(a)
    left = [1] * n
    right = [1] * n
    prod = [1] * n
    for i in range(1,len(a)):
        left[i] = a[i-1] * left[i-1]
    for i in range(n-2,-1,-1):
        right[i] = right[i+1] * a[i+1]
    
    for i in range(len(a)):
        prod[i] = left[i] * right[i]   
    print(left,right)
    print(prod)
        
    
def solve_with_more_optimized(a):
    n = len(a)
    prod = [1] * n
    temp = 1
    for i in range(n):
        prod[i] = temp
        temp *= a[i]

    print("prod array alias left sum", prod)
    temp = 1
    for i in range(n-1,-1,-1):
        prod[i] *= temp
        temp *= a[i]
    print("final prod is ")
    print(prod)
    
    
    # n = len(a)
    # prod = [1] * n
    # temp = a[0]
    # for i in range(1,n):
    #     prod[i] = temp
    #     temp *= a[i]

    # temp = 1
    # for i in range(n-1,-1,-1):
    #     prod[i] *= temp
    #     temp *= a[i]
    # return prod
    
    
a = [10,3,5,6,2]
solve_with_brute_force(a)
solve_with_optimized(a) # time and space complexity are o(n) and o(n)
solve_with_more_optimized(a)

