import pickle

while True:
    question = input("Giriş Yap (1) / Kayıt Ol (2): ")
    if question == "2":
        with open("Log File.bin", "wb") as file:
            account_name = input("Kullanıcı Adı Giriniz: ")
            password = input("Şifre Giriniz: ")
            temporary_list = list()
            temporary_list.append(account_name)
            temporary_list.append(password)
            pickle.dump(temporary_list, file)

    elif question == "1":
        with open("Log File.bin", "rb") as file_object:
            account_name2 = input("Kullanıcı Adı: ")
            password2 = input("Şifre: ")
            file_object = pickle.load(file_object)
            for search in file_object:
                print(search)
                if search[0] == account_name2 and search[1] == password2:
                    print(f"Hoş Geldiniz {account_name2}")
