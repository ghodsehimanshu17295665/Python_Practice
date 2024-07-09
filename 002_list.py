l1 = [10, 20, 30, 40, 50, 60, 70]
list1 = ["abc", 34, True, 40, "male"]

# List Slicing:-
print(l1[1]) # 20
print(l1[-1]) # 70
print(l1[2:])# 30,40,50,60,70
print(l1[2:5])# 30,40,50
print(l1[:4]) #10,20,30,40
print(l1[-4:-1])# 40,50,60

#Change list Item :-
#Change the second item:
l1[1] = 100
print(l1)

#Change a Range of Item Values
print(list1)
list1[2:4] = [False, "banana"]
print(list1)

#insert() method:-inserts an item at the specified index:
l1.insert(1, "watermelon")
l1.insert(2,300)
print(l1)

a = [10,20,30,40,50]
a.insert(1,100)
print(a)

a.insert(2, 1000)
print(a)

# append() Method:- To add an item to the end of the list.
a.append(200)
print(a)

# extend() Method:-adds items of an iterable (list, tuple, dictionary, etc) 
# at the end of a list.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

a = [10,20,30,40]
b = [30,60,70,80,100]
a.extend(b)
print(a)

a = [10,20,30,40]
b = [30,60,70,80,100]
a.append(b)
print(a)


#remove() method removes the specified item.
l = [10,20,20,30,60,800,90,2098,34]
print(l)
l.remove(20)
print(l)

#pop() method removes the specified index.
l.pop(5)
print(l)

#If you do not specify the index, 
# the pop() method removes the last item.
l.pop()
print(l)

#del keyword also removes the specified index:
del l[0]
print(l)

#del keyword can also delete the list completely.
del list1
#print(list1)

#sort() the list alphanumerically, ascending.
l1 = [50,89,74,15,23,45,96,410,78,0,421]
l1.sort()
print(l1)

#sort descending, use the keyword argument reverse = True
l1.sort(reverse=True)
print(l1)

#reverse() method reverses the sorting order of the elements.
a = [10,20,30,40,50]
a.reverse()
print(a)
