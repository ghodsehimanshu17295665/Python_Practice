#Python sets:-

thisset = {"apple", "banana", "cherry",True, 1, 2}
print(thisset)
print(len(thisset)) 
print(type(thisset))

#Access Set Items:-
#You cannot access items in a set by referring to an index or a key.

for x in thisset:
  print(x) 


# Add Set Items :- 
# 1.add() method:- add one item to a set use the add() method.
thisset.add("orange")
print(thisset)

# 2.update()method:-add items from another set into the current set,use the update()method.
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) 

#Remove Set Items :-
#1.remove():- 
thisset.remove("banana")
print(thisset) 

#2.discard() :-
thisset.discard("pineapple")
print(thisset) 

#3.pop() method :-
thisset.pop()
print(thisset)


#Python - Join Sets :-------------


#union() method :- returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) 

#Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

#update()method:- inserts all items from one set into another.
#update() changes the original set, and does not return a new set.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1) 

#intersection() method:- will return a new set, 
# that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple","banana"}
set3 = set1.intersection(set2)
print(set3)

#intersection_update() method :- will also keep ONLY the duplicates, 
# but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

#difference()method:-will return a new set that will contain 
# only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

#difference_update()method:- will also keep the items from 
# the first set that are not in the other set, 
# but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

#symmetric_difference()method:-will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3) 

#symmetric_difference_update() method:- will also keep all but the duplicates, 
# but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)