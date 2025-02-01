# ## Problem Statement
# WAP for number if even or odd (%2==0)

num = int(input("Enter the number:"))

if num > 0:
    print("The number is Positive.")
    if num %2==0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is zero or negative")
# WAP for find the leap year [divided by 4 and remainder is 0 ]


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input("Enter the year:"))
if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
year = int(input("Enter the year:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, 'this is a leap year')
        else:
            print(year, ' this year is not leap year')
    else:
        print(year, 'this is leap year')
else:
    print(year, "this is not leap year")