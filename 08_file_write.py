# File Handling:- Writing For a File.

file2 = open("write.txt", "w")

# 1. write()
file2.write("This is the Write command\n")
file2.write("Hello, World!\n")
file2.write("This is a sample file.\n")

# 2. writelines():
lines = ["First line.\n", "Second line.\n", "Third line."]
file2.writelines(lines)


# Example of Writing to a File with the with Statement:-
with open("write1.txt", "w") as file2:
    file2.write("Hello, World!\n")
    file2.write("This is a sample file.\n")

file2.close()
