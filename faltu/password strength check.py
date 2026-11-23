password = input("Enter your password: ")

if len(password) < 8:
    print("Weak password")
else:
    has_upper = False
    has_number = False

    for ch in password:
        if ch.isupper():
            has_upper = True

        if ch.isdigit():
            has_number = True

    if has_upper and has_number:
        print("Strong password")
    else:
        print("Medium password")