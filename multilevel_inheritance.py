class grandparent:
    def __init__(self) -> None:
        print("in the grand parent")

class parent(grandparent):
    def __init__(self) -> None:
        super().__init__()
        print("in the parent")
        
    
class child(parent):
    def __init__(self) -> None:
        super().__init__()
        print("in the child")
        

child_obj=child()
