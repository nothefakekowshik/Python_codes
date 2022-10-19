import sys
class library:
    def take_cs01(self,books_details,count_books):
        if(count_books>books_details["CS01"]):
            print("\nSorry for the incoveinece! Number of books available are %d" %(books_details["CS01"]))
        else:
            print("Thank you for using our service! Please use our book properly")
            print("\nYou took %d books" %(count_books))
            books_details["CS01"]-=count_books


    def give_back_cs01(self,books_details,count_books):
        if(count_books>5):
            print("\nYou cant return more than 5 books")
        elif(books_details["CS01"]+count_books<=5):
            print("\nThank you for using our service!")
            print("\nYou returned %d books" %(count_books))
            books_details["CS01"]+=count_books
        else:
            print("The shelf in the library is overflowed")


        
    
    def take_cs02(self,books_details,count_books):
        if(count_books>books_details["CS02"]):
            print("\nSorry for the incoveinece! Number of books available are %d" %(books_details["CS02"]))
        else:
            print("Thank you for using our service! Please use our book properly")
            print("\nYou took %d books" %(count_books))
            books_details["CS02"]-=count_books
        pass

    def give_back_cs02(self,books_details,count_books):
        if(count_books>5):
            print("\nYou cant return more than 5 books")
        elif(books_details["CS02"]+count_books<=5):
            print("\nThank you for using our service!")
            print("\nYou returned %d books" %(count_books))
            books_details["CS02"]+=count_books
        else:
            print("The shelf in the library is overflowed")
        


    def take_cs03(self,books_details,count_books):
        if(count_books>books_details["CS03"]):
            print("\nSorry for the incoveinece! Number of books available are %d" %(books_details["CS03"]))
        else:
            print("Thank you for using our service! Please use our book properly")
            print("\nYou took %d books" %(count_books))
            books_details["CS03"]-=count_books
        pass

    def give_back_cs03(self,books_details,count_books):
        if(count_books>5):
            print("\nYou cant return more than 5 books")
        elif(books_details["CS03"]+count_books<=5):
            print("\nThank you for using our service!")
            print("\nYou returned %d books" %(count_books))
            books_details["CS03"]+=count_books
        else:
            print("The shelf in the library is overflowed")

    def menu(self,books_details):
        print("\nAvailable books are ")
        for i,j in books_details.items():
            print("%s --> %d" %(i,j))
        print("Enter q to exit or enter the book name you want to take or return back\n")





lib=library()
books_details={
    "CS01":5,
    "CS02":5,
    "CS03":5,
}

lib.menu(books_details)

while True:
    option=input().upper()
    if(option=='q' or option=='Q'):
        print("Thank you")
        exit(0)
    
    elif(option=="CS01"):
        print("You chose the book CS01")
        give_or_take=input("Enter g to give and t to take").lower()
        if(give_or_take=='g'):
            count_books=int(input("How many books do you want to give?"))
            lib.give_back_cs01(books_details,count_books)
            lib.menu(books_details)
        elif(give_or_take=='t'):
            count_books=int(input("How many books do you want to take?"))
            
            lib.take_cs01(books_details,count_books)
            lib.menu(books_details)

            
    elif(option=="CS02"):
        print("You chose the book CS02")
        give_or_take=input("Enter g to give and t to take").lower()
        if(give_or_take=='g'):
            count_books=int(input("How many books do you want to give?"))
            
            lib.give_back_cs02(books_details,count_books)
            lib.menu(books_details)
        elif(give_or_take=='t'):
            count_books=int(input("How many books do you want to take?"))
            
            lib.take_cs02(books_details,count_books)
            lib.menu(books_details)
    
    elif(option=="CS03"):
        print("You chose the book CS03")
        give_or_take=input("Enter g to give and t to take").lower()
        if(give_or_take=='g'):
            count_books=int(input("How many books do you want to give?"))
            lib.give_back_cs03(books_details,count_books)
            lib.menu(books_details)
        elif(give_or_take=='t'):
            count_books=int(input("How many books do you want to take?"))
            lib.take_cs03(books_details,count_books)
            lib.menu(books_details)
    