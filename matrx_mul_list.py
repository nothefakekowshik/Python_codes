t=int(input())
while t:
    t-=1
    n1,m1=list(map(int,input().split()))
    mat1=[]
    for i in range(n1):
        a=[]
        mat1.append(list(map(int,input().split())))
    n2,m2=list(map(int,input().split()))
    mat2=[]
    for i in range(n2):
        a=[]
        mat2.append(list(map(int,input().split())))
    res=[]
    for i in range(n1):
        temp=[0]*m2
        res.append(temp)
    for i in range(n1):
        for j in range(m2):
            for k in range(n2):
                res[i][j]+=mat1[i][k]*mat2[k][j]
            print(res[i][j],end=" ")
        print()
    
       
        
            
            