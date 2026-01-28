# Program that reads the age and informs if the person still needs to enlist,
# if it's time to enlist, or if the enlistment period has already passed,
# and prints how many years are left or overdue

from datetime import date

birth_year = int(input('What is your year of birth? '))
age = date.today().year - birth_year
remaining = 18 - age

print('You are {} years old.'.format(age))

if age < 18:
    print('You still need to enlist, {} years left.'.format(remaining))
elif age == 18:
    print('It is time to enlist.')
else:
    overdue = age - 18
    print('You are {} years past the enlistment period!'.format(overdue))