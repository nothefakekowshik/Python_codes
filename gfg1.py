# code
t = int(input())
while t:
    n1 = int(input())
    a1 = []
    x = 0
    for i in range(n1):
        x = int(input())
        a1.append(x)
    n2 = int(input())
    a2 = []
    y = 0
    for i in range(n2):
        y = int(input())
        a2.append(y)
    ma = max(a1)
    mi = min(a2)
    print(ma * mi)
    t -= 1
