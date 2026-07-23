def has_number(password):
    for character in password:
        print(character)
        if character.isdigit():
            True
    return False

password = input("Enter password: ")

if has_number(password):
    print("Password contains a number")
else:
    print("Password does not contain a number")