# https://www.codechef.com/FEB221C/problems/BINBASBASIC

def check(n,cnt,k):
    if(cnt > k):
        return False
    else:
        if(n%2==1):
            return True
        if((k-cnt) %2==0):
            return True
        return False

t=int(input())
while t:
    t-=1
    lenn,k=list(map(int,input().split()))
    n=input()
    low=0
    high=len(n)-1
    diff_count=0
    while(low<high):
        if(n[low]!=n[high]):
            diff_count+=1
        low+=1
        high-=1
    if(check(len(n),diff_count,k)):
        print("YES")
    else:
        print("NO")

    
