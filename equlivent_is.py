# The "is" keyword is used to check if two variables refer to the same object in memory.
# Use the == operator to check if the values of two variables are equal.


x=[5,7,9]
y=x
z=[5,7,9]
print(x==y)
print(x is y)













# The id() function returns a unique id for the specified object.
# All objects in Python has its own unique id.
#Immutable objects can have the same "id" if their values are the same
# Mutable objects such as (lists and dictionaries) can have unique "id" even if their values are the same.

list1=[2,"a",6]
list2=[2,"a",6]
#print(id(list1))
#print(id(list2))

tuple1=(2,"a",6)
tuple2=(2,"a",6)
#print(id(tuple1))
#print(id(tuple2))