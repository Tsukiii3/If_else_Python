# Program that calculates the price of a product based on the payment method

prod = float(input('What is the price of the product? '))

print('Enter 1 - Cash or check (10% discount)')
print('Enter 2 - Card payment upfront (5% discount)')
print('Enter 3 - Up to 2 installments on the card (normal price)')
print('Enter 4 - 3 or more installments on the card (20% interest)')

op = int(input('Enter the payment method: '))

if op == 1:
    prod = prod - (prod * 10 / 100)
    print('PROCESSING...................')
    print('The total price will be {}'.format(prod))
elif op == 2:
    prod = prod - (prod * 5 / 100)
    print('PROCESSING...................')
    print('The total price will be {}'.format(prod))
elif op == 3:
    installment = prod / 2
    print('PROCESSING...................')
    print('The total price will be {}'.format(prod))
    print('The value of each installment will be {}'.format(installment))
elif op == 4:
    prod = prod + (prod * 20 / 100)
    print('PROCESSING...................')
    print('The total price will be {}'.format(prod))
else:
    print('ENDING OPERATION...............')
    print('PLEASE ENTER THE PRODUCT PRICE AGAIN AND SELECT A VALID METHOD')