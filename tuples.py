# Tuples are similar to lists but are not mutable we wil cover this later for now
# lets create a simple tumple in python!
tuple1 = ("disco",10,1.2)
print(tuple1)
print(type(tuple1))
# Each element of the tuple can also be accesed via index just like a list 
print(f"Accessing the first element {tuple1[0]}")
print(f"Accessing the second element {tuple1[1]}")
print(f"Accessing the third element {tuple1[2]}")
print("We can also print out the type of each element inside a tuple ")
print(f"Type of first element of the tuple {type(tuple1[0])}")
print(f"Type of second element of the tuple {type(tuple1[1])}")
print(f"Type of third element of the tuple {type(tuple1[2])}")
# just like lists we can also use negative indexing to access the elements of a 
# tuple 
print(f"Accessing the first element of the tuple using negative index {tuple1[-3]}")
print(f"Accessing the second element of the tuple using negative index {tuple1[-2]}")
print(f"Accessing the third element of the tuple using negative index {tuple1[-1]}")