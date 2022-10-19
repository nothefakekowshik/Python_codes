dict={}
str="rgbbgyy"
for i in range(len(str)):
    dict[str[i]]=0
for i in range(len(str)):
    dict[str[i]]+=1
for i in range(len(str)):
    if(dict[str[i]]%2==1):
        print(str[i])
        break