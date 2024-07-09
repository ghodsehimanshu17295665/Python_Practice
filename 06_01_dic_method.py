# Dictionary Method:-

#clear() method removes all the elements from a dictionary.
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.clear()
print(car)

#copy() method returns a copy of the specified dictionary.
car = {
    "brand" : "ford",
    "model" : "abc",
    "year" : 2024
}
x = car.copy()
print(x)

#get() method returns the value of the item with the specified key.
print(car.get('brand'))
print(car.get('model'))
print(car.get('year'))

#items() method returns a view object. 
# The view object contains the key-value pairs of the dictionary as tuples in a list.
print(car.items())

#keys() method returns a view object. 
#The view object contains the keys of the dictionary, as a list.
print(car.keys())

#pop() method removes the specified item from the dictionary.
car.pop('model')
print(car)

#popitem() method removes the item that was last inserted into the dictionary. 
car.popitem()
print(car)

#The setdefault() method returns the value of the item with the specified key.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault('model')
print(x)

x =car.setdefault('model', 'Bronco')
print(x)

x = car.setdefault("color", "white")
print(x) 

# update() method inserts the specified items to the dictionary.
print(car)

car.update({"company":"TCS"})
print(car)

car.update({"year":2023})
print(car)

#values() method returns a view object. 
# The view object contains the values of the dictionary, as a list.

print(car.values())
print(car.keys())
print(car)
