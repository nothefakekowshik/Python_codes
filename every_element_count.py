a=[-9,10,8,6,7,8]
queries=[-1,10,8,15,20]
freq={}
for i in a:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
for i,j in freq.items():
    print("%d  %d" %(i,j))
print("count")
for i in queries:
    if i not in a:
        print("0")
    else:
        print(freq[i])


