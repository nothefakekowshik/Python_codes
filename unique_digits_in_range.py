l,h=10,20
for i in range(l,h+1):
    if(len(str(i))==len(set(str(i)))):
        print(i)
