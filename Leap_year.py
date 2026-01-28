from datetime import date

year = int(input('Enter the year you want to check, or 0 to check the current year: '))

if year == 0:
    year = date.today().year
if year % 4 == 0:
    print('The year {} is a leap year.'.format(year))
else:
    print('The year {} is NOT a leap year.'.format(year))