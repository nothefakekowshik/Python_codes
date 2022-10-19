a=[
    [1,1],
    [1,1],
    [1,1]
]
for i in range(3):
    for j in range(2):
        print(a[i][j],end=" ")
    print()
print()
print(len(a[0]))
print("transpose")
for i in range(len(a[0])):
    for j in range(3):
        print(a[j][i],end=" ")
    print()