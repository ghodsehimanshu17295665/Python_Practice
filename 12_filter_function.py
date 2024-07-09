#filter() in python :-

# Using filter() with a lambda function to filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
# Converting filter object to list to see the result
even_numbers_list = list(even_numbers)
print(even_numbers_list)

print('\n')

# Using filter() to remove None values from a list
values = [1, None, 0, None, 3, None, 8, None]
filtered_value = filter(None,values)
# Converting filter object to list to see the result
filtered_value_list = list(filtered_value)
print(filtered_value_list)