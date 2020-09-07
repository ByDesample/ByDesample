file = open("küfür.txt", "r", encoding="utf-8")

kelime = ""
while True:
    bannedWord = file.readline()
    if bannedWord == "":
        break
    else:
        kelime += bannedWord


string = input("Enter word: ")
words = string.split()
string = ""
for word in words:
    if word in kelime:
        string += "*** "
    else:
        string += f"{word} "
print(string)