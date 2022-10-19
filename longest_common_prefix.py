def check(strs):
    min_len=len(strs[0])
    for i in strs:
        min_len=min(min_len,len(i))
    result=""
    for i in range(min_len):
        current=strs[0][i]
        for j in range(1,len(strs)):
            if(strs[j][i]!=current):
                return result
        result+=current
    return result

strs=["flight","flow","flower"]
print(len(check(strs)))


    
    