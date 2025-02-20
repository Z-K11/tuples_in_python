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
# Tuples can be concatenated and combined using the "+" signt
tup =tuple1 + ("Dwayne the rock jhonson","tom")
print(tup)
# Tuples can also be sliced 
print(f"Printhing the 2nd,3rd and 4th element of the tuple {tup[2:5]}")
print(f"To obtain length of the tuple use len(x), the length is  {len(tup)}")
# A tuple can also be sorted 
tupele = (5,2,7,5,1,2,8,5,4,1,2,0,9,8,5)
tupele = sorted(tupele)
print(tupele)
# Nested tuple 
tuple1 = (0,1,2,(2,4),2,(4,'a'))
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])
print(tuple1[4])
print(tuple1[5])
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
# Print element on each index, including nest indexes

print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])