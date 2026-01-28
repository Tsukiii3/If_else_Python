
km = float(input('What is the distance of the trip in km? '))

if km <= 200:
    km = km * 0.50
    print('The total to pay is {}'.format(km))
else:
    km = km * 0.45
    print('The total to pay is {}'.format(km))