a="geeksforgeeks"
b="gksrek"

len_a=len(a)
len_b=len(b)
i,j=0,0

while(i<len_a and j<len_b):
    if(a[i]==b[j]):
        i+=1
    j+=1
print(j)
print(j==len_b)