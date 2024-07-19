# Exception handling :-

try:
    # Attempt to divide by zero
    numerator = 10
    denominator = 0
    result = numerator / denominator
except ZeroDivisionError as e:
    # Handle the error if division by zero occurs
    print(f"An error occurred: {e}")
finally:
    # This block will always execute
    print("Execution of try-except-finally block is complete.")
