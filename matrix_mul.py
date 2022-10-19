rows1=int(input("Enter the number of rows"))
columns1=int(input("Enter the number of columns"))
matrix1=[]
matrix2=[]
for i in range(rows1):
    a=[]
    for j in range(columns1):
        a.append(int(input()))
    matrix1.append(a)
rows2=int(input("Enter the number of rows"))
columns2=int(input("Enter the number of columns"))
if(columns1==rows2):
    for i in range(rows2):
        a=[]
        for j in range(columns2):
            a.append(int(input()))
        matrix2.append(a)
    res=[]
    for i in range(rows1):
        a=[]
        for j in range(columns2):
            a.append(0)
        res.append(a)
    for i in range(rows1):
        for j in range(columns2):
            for k in range(columns1):
                res[i][j]=int(res[i][j])+int(matrix1[i][k])*int(matrix2[k][j])
    c=1
else:
    c=0
if(c==1):
    print("Result is ")
    for i in range(rows1):
        for j in range(columns2):
            print(res[i][j],end=" ")
        print()
else:
    print("Multiplication not possible")