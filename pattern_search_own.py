txt='hello'
pat='el'
flag=0
txt_count=0
pat_count=0
for i in pat:
    pat_count+=ord(i)
for i in range(len(pat)):
    txt_count+=ord(txt[i])

if(txt_count==pat_count):
    flag=1
    start=i-len(pat)+1
    end=i
    print("found")
    print("from {} to {}".format(start,end))
else:
    for i in range(len(pat),len(txt)):
        txt_count=txt_count-ord(txt[i-len(pat)])+ord(txt[i])
        if(txt_count==pat_count):
            start=i-len(pat)+1
            end=i
            flag=1
            break

    if(flag==1):
        print("found")
        print("from {} to {}".format(start,end))
    elif(flag==0):
        print("not found")