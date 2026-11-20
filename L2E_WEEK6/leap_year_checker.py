user_year_str = input('Enter year: ')
year = int(user_year_str)
is_leap = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
        else:
            is_leap = False
    else:
        is_leap = True
else:
    is_leap = False

if is_leap == True:
    print(f'{year}, is a leap year')
else:
    print(f'{year}, is not a leap year')

    

found_count = 0
check_year = year + 1

print('The next 3 leap years are:')
while found_count < 3:
    if check_year % 4 == 0 and (check_year % 100 != 0 or check_year % 400 == 0):
        print(check_year)
        found_count += 1
    check_year +=1
