l1 = [10, 20, 30, 40, 50, 60, 70]
list1 = ["abc", 34, True, 40, "male"]
print(l1)
print(list1)
print(type(l1))

#Access List Item:-

print(l1[1])
print(l1[-1])
print(l1[2:])
print(l1[2:5])
print(l1[:4])
print(l1[-4:-1])

#Change list Item :-
#Change the second item:
l1[1] = 100
print(l1)

#Change a Range of Item Values
print(list1)
list1[2:4] = [False, "banana"]
print(list1)

#Insert Item:- 
l1 = [10, 20, 30, 40, 50, 60, 70]

#insert() method:-inserts an item at the specified index:
l1.insert(1, "watermelon")
l1.insert(2,300)
print(l1)

#append() method:- To add an item to the end of the list.
l1.append('orange')
print(l1)

#extend() method:-To append elements from another list to the current list
l1.extend(list1)
print(l1)

list2 = ['A','B','C']
list1.extend(list2)
print(list1)

#Python - Remove List Items:-
#remove() method:- removes the specified item.
print(l1)
l1.remove('banana')
print(l1)

#pop() method:- removes the specified index.
l1.pop(1)
print(l1)
#If you do not specify the index, the pop() method removes the last item.
l1.pop()
print(l1)

#del keyword also removes the specified index:
del l1[1]
print(l1)

#clear() method empties the list.
list2.clear()
print(list2)

#Sort Lists:-
l2 = [100, 50, 65, 82, 23]
l2.sort()
print(l2)

#Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# sort descending, use the keyword argument reverse = True:
thislist.sort(reverse=True)
print(thislist)

l2.sort(reverse=True)
print(l2)

#Copy a List:-
mylist = thislist.copy()
print(mylist)

#Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)