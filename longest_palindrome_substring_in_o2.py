def bs(a,low,high):
    while(low>=0 and high<len(a) and a[low]==a[high]):
        low-=1
        high+=1
    return a[low+1:high]

def longestPalindrome(s):
    longest_substring=""
    if(len(s)==0 or len(s)==1):
        return s
    else:
        for i in range(len(s)):
            temp=bs(s,i,i)
            if(len(temp)>len(longest_substring)):
                longest_substring=temp
            temp=bs(s,i,i+1)
            if(len(temp)>len(longest_substring)):
                longest_substring=temp
        return longest_substring
            

print(longestPalindrome("forgeeksskeegfor"))
