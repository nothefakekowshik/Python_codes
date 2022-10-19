
def multiply2(n):
    while(n%2==0 and n>=2):
        n=n//2
    return n
def multiply5(n):
    while(n%5==0 and n>=5):
        n=n//5
    return n
def multiply3(n):
    while(n%3==0 and n>=3):
        n=n//3
    return n

ugly_numbers=[]
for i in range(1,7):
    ugly_numbers.append(i)
cnt=7
i=7
while True:
    if(cnt==151):
        break
    n=multiply2(i)
    n=multiply3(n)
    n=multiply5(n)
    if(n==1):
        ugly_numbers.append(i)
        cnt+=1
    i+=1

k=int(input("Enter the index"))
print(ugly_numbers[k-1])

#Failed at 150th index