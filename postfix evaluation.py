t=int(input())
while t:
    l=input()
    stack=[]
    index=-1
    for i in l:
        if(i.isnumeric()):
            stack.append(i)
            index+=1
        else:
            if(i=='*'):
                stack[index-1]=int(stack[index-1])*int(stack[index])
                del stack[index]
                index-=1

            if(i=='+'):
                stack[index-1]=int(stack[index-1])+int(stack[index])
                del stack[index]
                index-=1

            if(i=='/'):
                stack[index-1]=int(stack[index-1])//int(stack[index])
                del stack[index]
                index-=1

            if(i=='-'):
                stack[index-1]=int(stack[index-1])-int(stack[index])
                del stack[index]
                index-=1
                
    print(stack[index])
    t-=1