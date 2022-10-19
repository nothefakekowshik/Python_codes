mydict={"Tetrahedron":4,"Cube":6,"Octahedron":8,"Dodecahedron":12,"Icosahedron":20}
n=int(input())
arr=[]
summ=0
for i in range(n):
    arr.append(input())
for i in arr:
    summ+=mydict[i]
print(summ)
