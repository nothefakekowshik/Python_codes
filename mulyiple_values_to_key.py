a=[92,4,14,24,44,91]
hashtable = [[] for i in range(len(a))]
hashsize=10

for i in a:
    rem=i%hashsize
    hashtable[rem].append(i)

for i in range(len(hashtable)):
    if(len(hashtable[i])!=0):
        print(i,end="")
        for j in hashtable[i]:
            print("->",end="")
            print(j,end="")
        print()





# o/p:
# 1->91
# 2->92
# 4->4->14->24->44