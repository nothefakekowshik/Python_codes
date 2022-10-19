s="3*3+2"
op_stack=[]
for i in s:
    op_stack.append(i)
op_stack=op_stack[::-1]
operators="+-*/"
for i in range(len(op_stack)-1):
    if op_stack[i]=="*":
        op_stack[i+1]=int(op_stack[i+1])*int(op_stack[i-1]) 
        i+=1
    if op_stack[i]=="/":
        op_stack[i+1]=int(op_stack[i+1])//int(op_stack[i-1]) 
        i+=1  
print(op_stack)     
print(op_stack[len(op_stack)-1])

