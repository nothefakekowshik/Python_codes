from abc import *

class shape(ABC):
    @abstractmethod
    def no_of_sides(self):
        pass

class traingle(shape):
    def no_of_sides(self):
        print("Traingle has 3 sides")

class square(shape):
    def no_of_sides(self):
        print("Sqaure has 4 sides")

t=traingle()
t.no_of_sides()
s=square()
s.no_of_sides()
