import csv

txt_file = "csv_data.txt"
output_file = "tex.csv"

# headers = ['id', 'name', 'age', 'mobile']

with open(txt_file, 'r') as file:
    data = file.readlines()
    lst = data[0].strip().split(',')
    # print(lst)

# print(data)

with open(output_file, 'w', newline='') as CSVfiles:
    csv_writer = csv.writer(CSVfiles)

    csv_writer.writerow(lst)
    for line in data[1:]:
        row = line.strip().split()
        csv_writer.writerow(row)

print(f"data Sucsessfully converted to {output_file}")
