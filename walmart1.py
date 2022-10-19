n=int(input())
q=[]
p=list(map(str,input().split()))
for i in range(len(p)):
    q.append(p[i])
m=int(input())
for i in range(m):
    pi=list(map(str,input().split()))
    if(pi[0]=="A"):
        q.pop(0)
    elif(pi[0]=="B"):
        curr_ind=q.index(pi[2])
        q.insert(curr_ind+1,pi[1])
    elif(pi[0]=="C"):
        q.insert(0,pi[1])

print(q)
