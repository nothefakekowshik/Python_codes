s=[1,2,1]
power_size=pow(2,len(s))


for i in range(power_size):
    temp=[]
    for j in range(len(s)):
        if(i&(1<<j)!=0):
            temp.append(int(s[j]))
    print(temp)
    
