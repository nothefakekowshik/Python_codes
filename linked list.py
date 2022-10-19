class Node:
    def __init__(self,value):
        self.info=value
        self.next=None

class linkedlist:
    def __init__(self):
        self.start=None

    def display(self):
        if self.start is None:
            print("\nList is empty")
        else:
            p=self.start
            while p is not None:
                print(p.info,end=" ")
                p=p.next

    def insertatbeg(self,data):
        if self.start is None:
            self.start=Node(data)
        else:
            temp=Node(data)
            temp.link=self.start
            self.start=temp

    def insertatend(self,data):
        if self.start is None:
            self.start=Node(data)
        else:
            p=self.start
            while p.next is not None:
                p=p.next
            p.next=Node(data)

    def createlist(self):
        n=int(input("\nEnter the number of nodes"))
        if n==0:
            print("\nNo nodes entered")
        for i in range(n):
            data=int(input("\nEnter the element values"))
            self.insertatend(data)

    def search(self,data):
        flag=0
        if self.start is None:
            print("The list is empty")
        else:
            p=self.start
            while p is not None:
                if(p.info==data):
                    flag=1
                    print("\nelement found")
                    break
                else:
                    p=p.next
            if(flag==0):
                print("\nElement not found")
                
Listobj=linkedlist()
Listobj.createlist()
print("\nDisplaying elements now")
Listobj.display()
print("\nSearching the element 3")
Listobj.search(3)
