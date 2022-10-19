for i in range(1,11):
    c=0
    for j in range(1,11):
        if(i%j==0):
            c+=1
    if(c==2):
        print(i,end=" ")