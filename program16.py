while True:
    try:
        first_number = input("First Number: ")
        islem = input("islem: ")
        second_number = input("Second Number: ")
        if islem == "+":
            print(f"Sonuç: {int(first_number) + int(second_number)}")
        elif islem == "-":
            print(f"Sonuç: {int(first_number) - int(second_number)}")
        elif islem == "*":
            print(f"Sonuç: {int(first_number) * int(second_number)}")
        elif islem == "/":
            print(f"Sonuç: {int(first_number) // int(second_number)}")
        else:
            print("Lütfen geçerli bir işlem giriniz.")
    except ZeroDivisionError:
        print("Hiç bir sayı 0'a bölünemez.")
