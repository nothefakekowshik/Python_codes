s="hello world I am kowshik"
temp_stack=[]
temp_val=" "
for i in range(len(s)-1,-1,-1):
    if(s[i]!=" "):
        temp_val+=s[i]
    else:
        temp_val=temp_val[::-1]
        temp_stack.append(temp_val)
        temp_val=" "

another_temp=""
for i in s:
    if i!=" ":
        another_temp+=i
    else:
        break
    
temp_stack.append(another_temp)
for i in temp_stack:
    print(i)



