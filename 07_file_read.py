# File Handling:- Reading For a File.

file1 = open("file1.txt", "r")

# 1. read()

print(file1.read(5))  # read 5 character for file
print(file1.read(5))
print(file1.tell())  # Returns current position of the file pointer in bytes.
file1.seek(0)  # Moves the file pointer to a specified position.
print(file1.read())


# 2. readline()
file1.seek(0)
print(file1.readline())
print(file1.readline())

# 3. readlines()
file1.seek(0)
print(file1.readlines())


# Opening a File with the with Statement:-
file1.seek(0)
with open("file1.txt", "r") as file1:
    data = file1.read()
print(data)

file1.close()
