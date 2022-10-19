a="abcd"
b="bcaa"
chars=[0 for i in range(256)]

for i in range(len(a)):

    chars[ord(a[i])]+=1
    chars[ord(b[i])]-=1

if 1 in chars:
    print("no")
else:
    print("yes`")
