# Reverses the entered numbers list.
#
# Author (s) : Cihat Buran
# email : cihattburann@gmail.com
# Last update : 2020.09.01

numbers = []
index = 1
while True:
    number = input("Enter an integer number: ")
    if number == "":
        break
    numbers.append(int(number))
print(numbers)




if len(numbers) > 1:
    print(numbers[::-1])