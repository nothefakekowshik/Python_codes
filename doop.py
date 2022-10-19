import random
num=[]
for i in range(1,91):
    r=random.randint(1,90)
    if r not in num:
        num.append(r)
num.sort()
print(num)
