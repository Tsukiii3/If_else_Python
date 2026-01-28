import random

pc = random.randint(0,5)
pl = int(input('Try to guess a number from 0 to 5 '))

print('PROCESS......')
print('The number chosen was {}'.format(pc))

if pl == pc:
    print('You guessed the number!')
    print('He just took home the R$1,000,000 prize.!')
else:
    print('You missed the number!!!!!!!')