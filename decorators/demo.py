from div import *

def smart_div(func,a,b):
    if(a<b):
        a,b=b,a
    func(a,b)

a,b=2,3

#div(a,b)

div=smart_div(div,a,b)



