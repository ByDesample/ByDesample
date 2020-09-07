# Calculates leap years from 2020 to 1900.
#
# Author (s) : Cihat Buran
# email : cihattburann@gmail.com
# Last update : 2020.08.24



def isLeapYear(year: str) -> bool:
    if year % 4 ==0:
        if year % 100 == 0:
            if year % 400 == 0 :
                return True
        return True
    return False


for year in range(2020,1900,-1):
    if isLeapYear(year):
        print(f"{year} is leap year")