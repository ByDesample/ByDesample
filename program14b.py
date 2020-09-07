with open("banned_words.txt") as dosya:
    banned_words = []
    while True:
        bannedWord = dosya.readline()
        if bannedWord == "":
            break
        else:
            banned_words.append(bannedWord)


    string = input("Enter word: ")
    words = string.split()
    string = ""
    for word in words:
        if word in banned_words:
            string += "*** "
        else:
            string += f"{word} "
print(string)
