from sys import flags


a=[]
def check(s):
    for i in range(len(s)):
        print(a)
        if(s[i]=='(' or s[i]=='{' or s[i]=='['):
            a.append(s[i])
        else:
            if a == []:
                return False
            # elif(a.pop=='(' and s[i]!=')'):   #True condition
            #     return False
            elif(s[i]==')' and a.pop()!='('):
                return False
            elif(s[i]==']' and a.pop() !='['):
                return False
            elif(s[i]=='}' and a.pop() !='{'):
                return False
    if len(a)==0:
        return True
    return False
                
s="[()]{}"
check(s)
if(len(a)==0):
    print("balanced")
else:
 print("not balanced")
























# def ispar(self,x):
#     s = x
#     a=[]
#     for i in range(len(s)):
    
#         if(s[i]=='(' or s[i]=='{' or s[i]=='['):
#             a.append(s[i])
#         else:
#             if a == []:
#                 return False
#             elif(s[i]==')' and a.pop()!='('):
                
#                 return False
            
#             elif(s[i]==']' and a.pop() !='['):
#                 return False
#             elif(s[i]=='}' and a.pop() !='{'):
#                 return False
#     if len(a)==0:
#         return True
#     return False

# s="[()]{}"
# print(ispar(s))






