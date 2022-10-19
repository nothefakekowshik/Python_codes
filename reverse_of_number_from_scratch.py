n=1225
rev_val=0
while(n>0):
    temp_val=n%10
    rev_val=rev_val*10+temp_val
    n=n//10
print(rev_val)