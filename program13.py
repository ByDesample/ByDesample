# 5 names are taken from the user. If the current name is written, it gives an error message.
#
# Author (s) : Cihat Buran
# email : cihattburann@gmail.com
# Last update : 2020.09.02

names = []
index = 1
while index < 6:
    name = input("Enter name: ")
    if name == "" and index > 5:
        break
    elif name == "":
        continue
    if name in names:
        print(f"Name \"{name}\" already exist")
        continue
    else:
        names.append(name)
        index += 1
print(names)