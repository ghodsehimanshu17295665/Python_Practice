
with open("input.txt", "r") as file:
    data = file.read()
    # print(data)
var = data.upper()

with open("output.txt", "w") as file1:
    file1.write(var)

lower_case_data = data.lower()
with open("output.txt", "w") as file:
    file.write(lower_case_data)
