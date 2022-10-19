def check(nums):
    if(len(nums)==1):
            return 1
    if(len(nums)==2):
        return 2
    front1,front2=0,0
    back1,back2=0,0
    if(nums.index(max(nums)) <= len(nums)-nums.index(max(nums))):
        #print(nums.index(max(nums)))
        front1=1
    elif(nums.index(max(nums)) > len(nums)-nums.index(max(nums))):
        back1=1
    
    if(nums.index(min(nums)) <= len(nums)-nums.index(min(nums))):
        front2=1
    elif(nums.index(min(nums)) > len(nums)-nums.index(min(nums))):
        back2=1

    print(front1,front2,back1,back2)
    print(max(nums),min(nums))

    if(front1 and front2):
        return max(nums.index(max(nums)),nums.index(min(nums)))+1
    if(back1 and back2):
        return len(nums)-min(nums.index(min(nums)),nums.index(max(nums)))+1
    else:
        summed=0
        print(nums.index(max(nums)),len(nums)-nums.index(max(nums)))
        print(nums.index(min(nums)),len(nums)-nums.index(min(nums)))
        summed+=min(nums.index(max(nums))+1,len(nums)-nums.index(max(nums)))
        summed+=min(nums.index(min(nums))+1,len(nums)-nums.index(min(nums)))
        return summed

#nums = [0,-4,19,1,8,-2,-3,5]
nums=[2,10,7,5,4,1,8,6]
#nums=[1,2,3,4,0,5]
nums=[42,-75] #expected : 2
nums=[-1,-53,93,-42,37,94,97,82,46,42,-99,56,-76,-66,-67,-13,10,66,85,-28] #expected :11
nums=[-14,61,29,-18,59,13,-67,-16,55,-57,7,74] #expected: 6
print(check(nums))

























#https://leetcode.com/contest/weekly-contest-269/problems/removing-minimum-and-maximum-from-array/