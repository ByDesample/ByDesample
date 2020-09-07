# Censored words.
#
# Author (s) : Cihat Buran
# email : cihattburann@gmail.com
# Last update : 2020.09.07

bannedWords = ["amk", "aq"]

string = input("Enter a sentence: ")

words = string.split()

string = ""

for word in words:
    if word in bannedWords:
        string += "*** "
    else:
        string += f"{word} "

print(string)