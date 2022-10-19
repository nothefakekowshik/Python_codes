a=33
res=""
while(a>0):
    res+=str(a%2)
    a=a//2
print(res[::-1])
    