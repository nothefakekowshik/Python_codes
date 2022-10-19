# 6
# 4 -2 10 12 -8 4 
# 8
# 176 -272 -272 -45 269 -327 -945 176 

n=6
a=[4,-2,10,12,-8,4]
freq={}

for i in a:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
for i,j in freq.items():
    print(i," ",j)