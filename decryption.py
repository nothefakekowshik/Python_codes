
sp="""abcdefghijklmnopqrstuv!"#$%&'()*+,-.MNOPQRSTUVWXYZ/:;<=>?@[\]^_`{|}~0123456789wxyzABCDEFGHIJKL""" 	

print("Enter the encrypted text:")
pat=input()
pat=pat.lstrip().rstrip()

newpat=""

for i in range(len(pat)):

    if(pat[i] in sp):
        newpat=newpat+sp[(sp.index(pat[i])-i)%len(sp)]

    elif(pat[i]=="\n"):
        newpat+="\n"
    
    else:
        newpat+=pat[i]

print()
print("Decryprted message is:")
print(newpat)
