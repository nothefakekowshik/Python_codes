def firstoccurence(a,i):
    for j in range(len(a)):
        if(a[j]!=i):
            return j
    

t=int(input())
while t:
    t-=1
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    for i in range(1,k+1):
        ugliness=0
        prev_back=firstoccurence(a,i)
        for v in range(prev_back+1,len(a)):
            if(a[v]!=i):
                if(a[v]!=a[prev_back] and v!=prev_back):
                    ugliness+=1
                    prev_back=v
                
        print(ugliness,end=" ")
    print()
                

#https://www.codechef.com/FZBZ21C/problems/CLESEQ                