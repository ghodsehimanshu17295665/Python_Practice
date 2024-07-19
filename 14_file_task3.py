# Content to write to the file
content = "BESTPEERS_InfoSystems_420@420.COM."

# Write the content to the file
with open("count.txt", 'w') as file:
    file.write(content)


def count(str):
    vowels = "AEIOUaeiou"
    digits = "0123456789"

    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    special_char_count = 0

    for char in str:
        if char in vowels:
            vowel_count += 1
        elif char in digits:
            digit_count += 1
        elif char.isalpha():
            consonant_count += 1
        else:
            special_char_count += 1

    total_char_count = len(str)

    return vowel_count, consonant_count, digit_count, special_char_count, total_char_count


file = "count.txt"

with open(file, 'r') as file1:
    content = file1.read()

vowel_count, consonant_count, digit_count, special_char_count, total_char_count = count(content)

# Print the results
print(f"Vowels Count: {vowel_count}")
print(f"Consonants Count: {consonant_count}")
print(f"Digits Count: {digit_count}")
print(f"Special Characters Count: {special_char_count}")
print(f"Total Characters Count: {total_char_count}")
