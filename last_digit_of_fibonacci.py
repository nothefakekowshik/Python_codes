n=100
a=0
b=1
count=0
for i in range(2,n+1):
    c=a+b
    a=b
    b=c
    count+=1
    if(n>=60 and count==60):

        print('Equal to 60 mowa')
        print()
    print(c)