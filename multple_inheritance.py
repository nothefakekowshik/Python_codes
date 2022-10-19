class parent1:
    def __init__(self) -> None:
        print("in the parent 1")

class parents2:
    def __init__(self) -> None:
        print("in the parent2 2")

class child(parent1,parents2):
    def __init__(self) -> None:
        print("in the child")
        super().__init__()

child_obj=child()

