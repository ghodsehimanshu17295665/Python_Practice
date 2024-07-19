# File Handling:- Appending For a File.

file = open("write.txt", "a")
file.write("\nAppending new content!")
file.close()


file = open("write2.txt", "a")
file.write("\nAppending new content!")

# Example of Appending to a File with the with Statement:-
with open("write1.txt", "a") as file:
    file.write("Appending new content!\n")

file.close()
