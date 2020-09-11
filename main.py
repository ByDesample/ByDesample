import pickle
import os


def DisplayMenu() -> None:
    print("1. Kayıtları Listele")
    print("2. Kayıt Ara")
    print("3. Kayıt Ekle")
    print("4. Kayıt Sil")
    print("5. Çıkış")
    print()


def MenuLoop() -> str:
    while True:
        DisplayMenu()
        option = input("Seçenek (1-5): ")
        print("\n")
        if option.isdigit() and 1 <= int(option) <= 5:
            break

    return option


def MainLoop():
    while True:
        option = MenuLoop()
        if option == "1":
            ListRecord()
        elif option == "2":
            SearchRecord()
        elif option == "3":
            AddRecord()
        elif option == "4":
            DeleteRecord()
        elif option == "5":
            break


def ListRecord() -> None:
    records_list = ReadFile()
    print(f"Kayıt Sayısı: {len(records_list)}\n")
    print(f"{'İsim':^10} {'Soyisim':^10} {'Telefon':^11}")
    for record in records_list:
        print(
            f"{record.get('name', ' '):10.10} {record.get('sur_name', ' '):10.10} : {record.get('tel_number', ' '):11.11}")
    print()


def SearchRecord() -> None:
    print("Kayıt Arama")
    name = input("İsim: ")
    sur_name = input("Soyisim: ")
    records_list = SearchRecordFromFile(name, sur_name)
    print("Telefon Numarası: ", end='')
    for record in records_list:
        print(f"{record.get('tel_number'):11.11}", end='')
    print("\n")


def AddRecord() -> None:
    print("Yeni Kayıt Ekle")
    name = input("İsim: ")
    sur_name = input("Soyisim: ")
    tel_number = input("Telefon Numarası: ")
    print(f"Yeni kayıt: {name} {sur_name}: {tel_number}")
    if AreYouSure():
        AddRecordToFile(name, sur_name, tel_number)
        print("Kayıt Eklendi\n")


def DeleteRecord() -> None:
    print("Kaydı Sil")
    name = input("İsim: ")
    sur_name = input("Soyisim: ")
    records_list = SearchRecordFromFile(name, sur_name)
    for record in records_list:
        print(f"{record.get('tel_number'):11.11}", end='')
    print("\n")
    if AreYouSure():
        DeleteRecordsFromFile(records_list)
        print("Kayıt Silindi\n")


def AreYouSure() -> bool:
    while True:
        answer = input("Emin misiniz? (E)vet/(H)ayır: ")
        print()
        if answer.upper() == "E":
            return True
        elif answer.upper() == "H":
            return False


def ReadFile() -> list:
    if os.path.isfile("data.bin"):
        with open("data.bin", "rb") as file_object:
            records_list = pickle.load(file_object)
        return records_list
    else:
        records_list = list()
    return records_list


def WriteFile(records_listP: list) -> None:
    with open("data.bin", "wb") as file_object:
        pickle.dump(records_listP, file_object)


def SearchRecordFromFile(nameP: str, sur_nameP: str) -> list:
    records_list = ReadFile()
    response_list = list()
    for record in records_list:
        if record.get("name").upper() == nameP.upper() and \
                record.get("sur_name").upper == sur_nameP.upper():
            response_list.append(record)
    return response_list


def AddRecordToFile(nameP: str, sur_nameP: str, tel_numberP: str) -> None:
    records_list = ReadFile()
    record_dict = dict(name=nameP, sur_name=sur_nameP, tel_number=tel_numberP)
    records_list.append(record_dict)
    WriteFile(records_list)


def DeleteRecordsFromFile(records_listP: list) -> None:
    records_list = ReadFile()
    for record in records_list:
        for recordForDelete in records_listP:
            if record.get("name") == recordForDelete.get("name") and \
                    record.get("sur_name") == recordForDelete.get("sur_name"):
                records_list.remove(recordForDelete)
                continue
    WriteFile(records_list)


MainLoop()
