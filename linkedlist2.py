class Node:
    def __init__(self,value):
        self.info=value
        self.link=None
class Linkedlist:
    def __init__(self):
        self.start=None
    def createlist(self):
        n=int(input("how many Nodes"))
        if n==0:
            return
        for i in range(n):
            data=int(input('enter the elements to be inserted'))
            self.insertend(data)
    def display(self):
        if self.start is None:
            print('empty list')
            return
        else:
            print('list is')
            p=self.start
            while p is not None:
                print(p.info,' ',end=' ')
                p=p.link
            print()
    def countnodes(self):
        if self.start is None:
            print("Empty list")
            return
        p = self.start
        n=0
        while p is not None:
            n+=1
            p = p.link
        print('number of nodes are',n)
    def search(self,x):
        pos=1
        p=self.start
        while p is not None:
            if p.info==x:
                print('found')
                return True
            pos+=1
            p=p.link
        else:
            print('element not found')
    def insertbeg(self,data):
        temp=Node(data)
        temp.link=self.start
        self.start=temp
    def insertend(self,data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
            return
        p=self.start
        while p.link is not None:
            p=p.link
        p.link=temp
    def insert_before_node(self,x,nodeval):
        temp=Node(x)
        p=self.start
        if self.start is None:
            self.start=temp
        else:
            while p.link is not None:
                if(p.link.info==nodeval):
                    temp.link=p.link
                    p.link=temp
                    break
                p=p.link
    def insert_after_node(self,x,nodeval):
        p=self.start
        temp=Node(x)
        if self.search is None:
            self.start=temp
        else:
            while p is not None:
                if(p.info==nodeval):
                    temp.link=p.link
                    p.link=temp
                    break
                p=p.link
    
    def delete_first_node(self):
        if self.start is None:
            return
        else:
            self.start=self.start.link
    def delete_last_node(self):
        p=self.start
        if self.start is None:
            return
        else:
            while p.link.link is not None:
                p=p.link
            p.link=None
    def delete_specific_node(self,x):
        p=self.start
        if self.start is None:
            return
        else:
            while p.link is not None:
                if(p.link.info==x):
                    p.link=p.link.link
                    break
                p=p.link
    
    
    def reverse_list(self):
        prev=None
        p=self.start
        while p is not None:
            next=p.link
            p.link=prev
            prev=p
            p=next
        self.start=prev
list=Linkedlist()
list.createlist()
while(1):
    print('\n1.Display \n 2.count \n 3.Search \n4.Insert at beg \n 5.Insert at end \n 6.Insert before a node \n 7.Insert after a node \
    \n 8.Delete the first node\n 9.Delete the last node \n 10.Delete a specific node\n 11.Reverse the list')
    option = int(input('enter the option'))
    if option == 1:
        list.display()
    elif option == 2:
        list.countnodes()
    elif option == 3:
        x = int(input('Enter the element to be searched'))
        list.search(x)
    elif option == 4:
        x = int(input('Enter the element to be inserted at the beginning'))
        list.insertbeg(x)
    elif option == 5:
        x = int(input('enter the element to be inserted at the ending'))
        list.insertend(x)
    elif option ==6:
        x=int(input("Enter the element to be inserted"))
        nodeval=int(input("Enter the node value that to be inserted before it"))
        list.insert_before_node(x,nodeval)
    elif option==7:
        x=int(input("Enter the element to be inserted"))
        nodeval=int(input("Enter the node value that to be inserted after it"))
        list.insert_after_node(x,nodeval)
    elif option==8:
        list.delete_first_node()
    elif option==9:
        list.delete_last_node()
    elif option==10:
        x=int(input("Enter the node values to be deleted"))
        list.delete_specific_node(x)
    elif option==11:
        list.reverse_list()
    else:
        print('Thank you')
        quit()