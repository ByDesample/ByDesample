while True:
    command = input("Bir işlem giriniz(sayı | işlem | sayı): ")

    if command == "":
        print("Kullanıcı Çıkışı.")
        break
    try:
        parse_command = command.split()

        number_1 = parse_command[0]
        operator = parse_command[1]
        number_2 = parse_command[2]

        try:
            if operator == "+":
                print(f"{number_1} + {number_2} = {int(number_1) + int(number_2)}")
            elif operator == "-":
                print(f"{number_1} - {number_2} = {int(number_1) - int(number_2)}")
            elif operator == "*":
                print(f"{number_1} * {number_2} = {int(number_1) * int(number_2)}")
            elif operator == "/":
                print(f"{number_1} / {number_2} = {int(number_1) / int(number_2)}")
        except ValueError:
            print("Geçersiz İşlem!")
    except IndexError:
        print("Geçersiz İşlem")