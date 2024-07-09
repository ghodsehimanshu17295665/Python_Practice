fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print('\n')

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
print('\n')

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

print('\n')

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#The range() Function:-
for i in range(6):
  print(i)

print("\n")
#Using the start parameter:
for x in range(2, 6):
  print(x)

print("\n")
for x in range(2, 30, 3):
  print(x)

#Nested Loops:-
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y) 

