
def leap_year(year):

    if year % 4 != 0:
        print("The entered year is not a leap year.")
    
    else:
        print(f"The year {year} is a leap year.")


print("Please enter the year you wish to check.")
enter_year = int(input())
leap_year(enter_year)