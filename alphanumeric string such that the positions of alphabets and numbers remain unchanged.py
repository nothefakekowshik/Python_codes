# Input: str = “geeks12for32geeks” 
# Output: eeeef12ggk23korss
# Input: str = “d4c3b2a1” 
# Output: a1b2c3d4 
 

str="geeks12for32geeks"
alphabets="abcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
al_a=[]
n_a=[]
for i in str:
    if i in alphabets:
        al_a.append(i)
    elif i in numbers:
        n_a.append(int(i))

al_a.sort()
n_a.sort()
j,k=0,0
for i in str:
    if i in alphabets:
        print(al_a[j],end="")
        j+=1
    elif i in numbers:
        print(n_a[k],end="")
        k+=1

