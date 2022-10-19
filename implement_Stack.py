n=8
for i in range(n):
    query=list(map(str,input().split()))
    
t=int(input())
stack=[]
while t:
    t-=1
    query=list(map(str,input().split()))
    
    if(query[0]=="push"):
        stack.append(query[1])
    
    elif(query[0]=="pop"):
        if(len(stack)==0):
            print("Empty")
        else:
            print(stack.pop())
            
#For each "pop" operation, print the popped element, separated by newline. If the stack is empty, print "Empty".