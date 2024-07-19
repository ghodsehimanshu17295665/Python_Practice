while True:
    user_input = input("Enter tex.. ")

    with open("tex1.txt", "a+") as file:
        user_input = user_input + "\n"
        file.write(user_input)
    choice = input('Do you want to add more content ? (Y/N)')
    if choice not in "Yy":
        break
