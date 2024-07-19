"""
Write a method in python to read lines from a text file INDIA.TXT, to find and
display the occurrence of the word “India”.
For example:
If the content of the file is
_________________________
“India is the fastest growing economy.
India is looking for more investments around the globe.
The whole world is looking at India as a great market.
Most of the Indians can foresee the heights that India is
capable of reaching.”
_________________________
The output should be 4
"""

with open("INDIA.txt", "r") as file:
    data = file.read()
    lst = data.split()


total_word = len(lst)

count = 0
for val in lst:
    if val.lower() == "india":
        count += 1

# Count occurrences of the letter "i" (case-insensitive)
i_count = data.count("i")

print(f"The Words India Count {count} times.")
print(f"Find frequency of i is {i_count}.")
print(f"Word Cont Total:- {total_word}.")
print(lst)
