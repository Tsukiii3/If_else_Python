
car = float(input('How fast are you driving? '))

print('============================= SIGN 80KM/H==========================================')
print('ANALYSING.............................')

if car <=80.0:
    print('You are within the limit, no ticket has been applied.')
    print('============================= LIMIT 80KM/H==========================================')
else:
    print('You.re out of bounds ')
    ticket = (car - 80) * 7
    print('You got a speeding ticket {:.2f}R$'.format(ticket))
    print('============================= LIMIT 80KM/H==========================================')