def check(a):
    if(a<=1):
        return False
    for i in range(2,a//2+1):
        if(a%i==0):
            return False
    return True


s=input("enter a number")
nums=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        nums.append(s[i:j])

ans=[]
print("prime numbers are")
for i in nums:
    temp=int(i)
    if(check(temp) and temp not in ans):
        ans.append(temp)
print(sorted(ans))
        
        


