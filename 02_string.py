#Python string:-

print("It's Alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello" #You can assign a multiline string to a variable by using three quotes:
print(a) 
print(len(a))

#String Slicing:-
b = "Hello, World!"
print(len(b))
print(b[2:5])
print(b[2:])
print(b[:2])
print(b[-5:-2])
print(b[-8:])
print(b[:-8])

#Modify String:-
a = "Hello, World!"
print(a.upper())
print(a.lower())

#Remove whitespace
#The strip() method removes any whitespace from the beginning or the end:
a = "  Hello, World!  "
print(a.strip()) # returns "Hello, World!"


#replace() method replaces a string with another string:
b = "Hello, World!"
print(b.replace('H','J'))

#split() method split a string into a list.
print(b.split(','))

#String Concatenation:
var1 = "Hello "
var2 = "Geek"
var3 = var1 + var2
print(var3)

var1 = "Hello"
var2 = "Geek"
var3 = var1 + " " + var2
print(var3)

#Format String:

age = 36
txt = f"My name is John, I am {age}"
print(txt) #Using F-String

#Placeholders and Modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 50
txt = f"The price is {price:.2f} dollars"
print(txt)

#String Methods :-

#1.capitalize()Method- Converts the first character to uppercase.
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x) 

#2. casefold() - Converts string into lower case
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#3.join() Method - 
#The join() method takes all items in an iterable and joins them into one string.
myTuple = ("John", "Peter", "Vicky")
x = " ".join(myTuple)
print(x) 
