s= "{()}[]"
a=[]
for i in s:
    if(i=='(' or i=='[' or i=='{'):
        a.append(i)
    else:
        if(len(a)==0):
            print("Not balanced")
            break
        elif(i==')'):
            if(len(a)-1=="("):
                a.pop()
        elif(i==']'):
            if(len(a)-1=="["):
                a.pop()
        elif(i=='}'):
            if(len(a)-1=="{"):
                a.pop()
print(a)       
if(len(a)==0):
    print("Not balanced")
else:
    print("not balanced")