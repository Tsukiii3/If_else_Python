
n1 = float(input('Enter a number: '))
n2 = float(input('Enter another number: '))
n3 = float(input('Enter another number: '))

low = n1
if n2 < n1 and n2 < n3:
    low = n2
if n3 < n1 and n3 < n2:
    low = n3
high = n1
if n2 > n1 and n2 > n3:
    high = n2
if n3 > n1 and n3 > n2:
    high = n3
print('The highest number is {}'.format(high))
print('The lowest number is {}'.format(low))