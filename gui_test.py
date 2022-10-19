from tkinter import *
from tkinter import filedialog


def encrypt(text_message):
    new_string=""
    dictt="abcdefghikjlmnopqrstuvwxyz"
    capital_alphabets="ABCDEFGHIKJkLMNOPQRSTUVWXYZ"
    for i in text_message:
        for charr in i:
            if(charr in dictt):
                new_string=new_string+dictt[(dictt.index(charr)+1)%26]
            elif(charr==" "):
                new_string+=" "
            elif(charr in capital_alphabets):
                new_string=new_string+capital_alphabets[(capital_alphabets.index(charr)+1)%26]
            elif(charr=="\n"):
                new_string+="\n"
            else:
                new_string+=charr
            

    file_output=open("output.txt","w")  
    file_output.write(new_string)
    selection = "Data modified and stored in output.txt file" 
    label.config(text = selection)
    label.pack()

    exit_button = Button(window, text="Exit", command=window.quit)
    exit_button.pack(pady=20)
    print(new_string)

def decrypt(text_message):
    new_string=""
    dictt="abcdefghikjlmnopqrstuvwxyz"
    capital_alphabets="ABCDEFGHIKJkLMNOPQRSTUVWXYZ"
    for i in text_message:
        for charr in i:
            if(charr in dictt):
                new_string=new_string+dictt[(dictt.index(charr)-1)%26]
            elif(charr==" "):
                new_string+=" "
            elif(charr in capital_alphabets):
                new_string=new_string+capital_alphabets[(capital_alphabets.index(charr)-1)%26]
            elif(charr=="\n"):
                new_string+="\n"
            else:
                new_string+=charr

    file_output=open("output.txt","w")  
    file_output.write(new_string)
    selection = "Data modified and stored in output.txt file" 
    label.config(text = selection)
    label.pack()

    exit_button = Button(window, text="Exit", command=window.quit)
    exit_button.pack(pady=20)
    print(new_string)

def openFile():
    print(var.get())
    filepath = filedialog.askopenfilename(
                                            initialdir="K:\pycharm\practice",
                                            title="Search for the txt file", 
                                            )
    file = open(filepath,'r')
    text_message=file.readlines()
    if(var.get()==1):
        encrypt(text_message)

    elif(var.get()==2):
        decrypt(text_message)
    file.close()

def sel():
    if(var.get()==1):
        selection = "You chose to encrypt " 
        label.config(text = selection)
        
    else:
        selection = "You chose to decrypt " 
        label.config(text = selection)
    

window = Tk() 
window.title("Cryptor")
window.geometry("1000x1000")

label = Label(window)
label.pack()

var = IntVar()

R1 = Radiobutton(window, text="Encrypt", variable=var, value=1,command=sel)
R1.pack( anchor = CENTER )

R2 = Radiobutton(window, text="Decrypt", variable=var, value=2,command=sel)
R2.pack( anchor = CENTER )

button = Button(text="OpenFile",command=openFile)
button.pack()
window.mainloop()