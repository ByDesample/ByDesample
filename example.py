import random

user_name = "bydesample"
password = "allah1dir"
i = 0

while True:
    input_user_name = input("User Name: ")
    input_password = input("Password: ")

    if user_name == input_user_name and password == input_password:
        print("Welcome")
        break
    elif user_name == input_user_name and password != input_password:
        print("Wrong password. Please try again")
        i += 1
    else:
        print("User not found! Please try again")
        i += 1

    if i == 5:
        print("Are you having trouble logging in?")
        trouble = input("(Y)es / (N)o: ")
        if trouble.upper() == "Y":
            verification_code = random.randint(99999, 999999)
            a = print(verification_code)
            verify = input("Verify: ")
            if verify == a:
                new_password = input("Please new password: ")
                password = new_password
        else:
            pass