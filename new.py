from os import write
new_string=""
def encrypt(i):
    global new_string
    dictt="abcdefghikjlmnopqrstuvwxyz"
    for charr in i:
        if(charr in dictt):
            new_string=new_string+dictt[(dictt.index(charr)+13)%26]
        elif(charr==" "):
            new_string+=" "
        

file_input=open("input.txt","r")
data=file_input.readlines()
print(data)
for i in data:
    encrypt(i)

# print("encrypted")
# print(new_string)

file_output=open("output.txt","w")  

file_output.write(new_string)
