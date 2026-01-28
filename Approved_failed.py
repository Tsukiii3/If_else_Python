n1 = float(input('Enter a first note'))
n2 = float(input('Enter another note'))
m = (n1+n2)/2
if m <7.5:
    print('Failed! Its your average was {}'.format(m))
else:
    print('Approved! Its your average was {}'.format(m))