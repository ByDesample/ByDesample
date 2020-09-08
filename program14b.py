with open("banned_words.txt", encoding="utf-8") as file:
    banned_words = []
    while True:
        bannedWord = file.readline()
        ban = bannedWord.split()
        if len(ban) >= 1:
            banned_words += ban
        else:
            break

    string = input("Enter word: ")
    words = string.split()
    string = ""
    for word in words:
        if word in banned_words:
            string += "*** "
        else:
            string += f"{word} "
print(string)
