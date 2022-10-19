# Input: ABC
# Output:
# ABC ACB BAC BCA CAB CBA

# Input: ABSG
# Output:
# ABGS ABSG AGBS AGSB ASBG ASGB BAGS 
# BASG BGAS BGSA BSAG BSGA GABS GASB 
# GBAS GBSA GSAB GSBA SABG SAGB SBAG 
# SBGA SGAB SGBA

str="ABC"
for i in range(len(str)):
    for j in range(len(str)):
            print(str[i],str[j],end=" ")
    print()     