from itertools import combinations
str1="kowshik"
str2="shikowk"
comb1=list(combinations(str1,1))
comb2=list(combinations(str2,1))
comb1.sort()
comb2.sort()
print(*(comb1))
print(*(comb2))
if(comb1==comb2):
    print("equal")