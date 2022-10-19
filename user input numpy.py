import numpy

my_array = []
a = int(input("Size of array:"))
for i in range(a):
    my_array.append(int(input("Element:")))
my_array = numpy.array(my_array)
print(numpy.floor(my_array))
print(my_array)