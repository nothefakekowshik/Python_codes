
sp="""abcdefghijklmnopqrstuv!"#$%&'()*+,-.MNOPQRSTUVWXYZ/:;<=>?@[\]^_`{|}~0123456789wxyzABCDEFGHIJKL""" 	
#print(len(sp))


#print("Enter the input")
#pat="Send guns,money and women.""\n""send bots too and contact me \n""9052584836"
pat="Hi kids! my name is chika chika slim shady. Excuse me! What? Can i have the attention of the class, my phone number is 905258"
#print(pat)
#print()

newpat=""

for i in range(len(pat)):
    if(pat[i] in sp):
        newpat=newpat+sp[(sp.index(pat[i])+i)%len(sp)]


    elif(pat[i]=="\n"):
        newpat+="\n"
    
    else:
        newpat+=pat[i]

print("Encrypted message:\n",newpat)
