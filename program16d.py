print("İşlem Giriniz (Çıkmak için Enter'a basınız).")
while True:
    command = input()

    if command == "":
        print("Kullanıcı Çıkışı.")
        break
    try:
        try:
            for i in command:
                if i == "+":
                    parse_command = command.split("+")
                    print(f"Sonuç : {float(parse_command[0]) + float(parse_command[1])}")
                elif i == "-":
                    parse_command = command.split("-")
                    print(f"Sonuç : {float(parse_command[0]) - float(parse_command[1])}")
                elif i == "*":
                    parse_command = command.split("*")
                    print(f"Sonuç : {float(parse_command[0]) * float(parse_command[1])}")
                elif i == "/":
                    parse_command = command.split("/")
                    print(f"Sonuç : {float(parse_command[0]) / float(parse_command[1])}")
        except ValueError:
            print("Geçersiz İşlem!")
    except IndexError:
        print("Geçersiz İşlem!")
