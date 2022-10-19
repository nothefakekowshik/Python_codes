r1=int(input("Enter the row 1"))
c1=int(input("Enter the row 2"))
print("Enter the matrix1")
matrix1=[]
for i in range(r1):
    
    matrix1.append(list(map(int,input().split())))
r2=int(input("Enter the row 2"))
c2=int(input("Enter the column 2"))
print("Enter the matrix2")
matrix2=[]
for i in range(r2):
    matrix2.append(list(map(int,input().split())))
res=[]
for i in range(r1):
    res.append([0]*c2)
print("result")
for i in range(r1):
    for j in range(c2):
        for k in range(r2):
            res[i][j]+=matrix1[i][k]*matrix2[k][j]
for i in range(r1):
    for j in range(c2):
        print(res[i][j],end=" ")
    print()