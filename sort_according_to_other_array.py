a=[2,1,2,5,7,1,9,3,6,8,8]
b=[2,1,8,3]
bs=" "
dict={}
for i in a:
    dict[i]=0
for i in a:
    dict[i]+=1
print(dict)
for i in b:
    if dict[i]>=1:
        temp=str(i)*dict[i]
        print(temp,end=" ")
        del dict[i]
print()
for i in sorted(dict.keys()):
    print(i,end=" ")