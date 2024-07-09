#Python Tuples :-
t1 = (1, 5, 7, 9, 3, 1, 2, 10, 10)
print(t1)
print(type(t1))
print(len(t1))

#One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


#Access Tuple Items:-
#You can access tuple items by referring to the index number, inside square brackets
print(t1[2])
print(t1[1])
print(t1[-1])
print(t1[2:])
print(t1[2:5])
print(t1[:4])
print(t1[-4:-1])

# Tuples are unchangeable, meaning that you cannot 
# change, add, or remove items once the tuple is created.


#Unpacking a Tuple :-
#When we create a tuple, we normally assign values to it. 
# This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry")
print(fruits)

#Unpacking a tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red) 

#Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

#Tuple Method:-
#1.count() returns the number of times a specified value appears in the tuple.
print(t1)
x = t1.count(10)
print(x)

#2.index()method finds the first occurrence of the specified value.
y = t1.index(9)
print(y)