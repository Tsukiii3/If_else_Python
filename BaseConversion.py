# Base conversion program: convert a decimal (base 10) number to binary, octal, or hexadecimal

num = int(input('Enter a base 10 number to convert: '))

print('Press 1 - for binary')
print('Press 2 - for octal')
print('Press 3 - for hexadecimal')
choice = int(input('Which base do you want to convert to? '))

if choice == 1:
    print('The number in binary is {}'.format(bin(num)[2:]))  # [2:] removes the first two characters
elif choice == 2:
    print('The number in octal is {}'.format(oct(num)[2:]))
elif choice == 3:
    print('The number in hexadecimal is {}'.format(hex(num)[2:]))
else:
    print('Invalid option, please try again.')