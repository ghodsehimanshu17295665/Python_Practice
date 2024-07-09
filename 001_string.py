print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)
print(type(a))
print(len(a))

#String Slicing in Python:-
str = "He is called Johnny"
print(str[::])
print(str[1:])
print(str[::5])
print(str[:3])

str1 = "HelloHowAreYou"
print(len(str1))
print(str1[1:5:2])
print(str1[1::2])
print(str1[-1:-12:-2])
print(str1[::-2])
print(str1[-5:-2])
print(str1[1:-1])

#Modify String :-
# upper() method:-
print(a.upper())
print(str.upper())

#lower() method:
print(a.lower())
print(str.lower())

#strip() method removes any whitespace from the beginning or the end:
b = "   Hello World     "
print(b.strip())

#replace() method replaces a string with another string:
print(a)
print(a.replace("H", "J"))

#split() method:-
a = "Hello World"
print(a.split(" "))

# Capitalize() method:-
print(a.capitalize())

#casefold() Method:
print(a.casefold())

#center() method:-
txt = "banana"
x = txt.center(20)
print(x)
print(txt.center(20,'k'))

#find() Method, index() Method:-

a = "Hello World"
print(a.find('W'))
print(a.find('H'))
print(a.find('z'))

print(a.index('W'))
#print(a.index('z')) Value error :- Substring not found. 

# Join() Method:-
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)


