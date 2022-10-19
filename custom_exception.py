class charNotPresent(Exception):
    pass

name = "kowshik"
try:
    print(name.index('a'))
    if('a'not in name):
        raise charNotPresent
        
except charNotPresent:
    print("search for the char that is present in the name")
except :
    print("caught by the inbuilt exception ")
finally:
    print("ok im in the finally")

print('ok bye')