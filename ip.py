ip=input()
lis=ip.split('.')
c=0
if(len(lis)==4):
    for i in lis:
        if(len(i)<=3):
            if (0 <= int(i) < 256):
                c+=1
if(c==4):
    print("1")