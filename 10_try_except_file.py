# Exception handling :-

try:
    file = open('example.txt', 'r')
    content = file.read()
except FileNotFoundError as e:
    print(f"An error occurred: {e}")
finally:
    if 'file' in locals() and file:
        file.close()
        print("File closed.")
