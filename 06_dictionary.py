#Python Dictionaries :-
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(len(thisdict))
print(type(thisdict))

#Access Dictionary Items:-
print(thisdict["brand"])
print(thisdict["model"])
print(thisdict["year"])

#get() method:- 
print(thisdict.get("model"))
print(thisdict.get("brand"))
print(thisdict.get("year"))

#Get Keys:-The keys() method will return a list of all the keys in the dictionary.
print(thisdict.keys())

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change 

#values() method:- will return a list of all the values in the dictionary.

print(thisdict.values())
print(car.values())

#items()method will return each item in a dictionary,as tuples in a list.
print(thisdict.items())
print(car.items())

#Change Dictionary Items :-
#Change Values:-
print(thisdict)
thisdict["year"] = 2018
print(thisdict)

#update() method will update the dictionary with the items from the given argument
thisdict.update({"year":2020})
print(thisdict)

car.update({"model": 'abc'})
print(car)

#Add Dictionary Items:-
thisdict["color"] = "red"
print(thisdict)

#Remove Dictionary Items:-
#pop() method:- removes the item with the specified key name
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item 
thisdict.popitem()
print(thisdict)

#del keyword removes the item with the specified key name:
del thisdict["year"]
print(thisdict) 

thisdict.update({"year":2020})
print(thisdict)

#Nested Dictionaries :-
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 
print(myfamily)
#Access Items in Nested Dictionaries :-
print(myfamily["child2"]["name"])
print(myfamily["child3"]["name"])
print(myfamily["child2"]["year"])