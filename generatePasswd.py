import string
import random

while True:
    try:
        tamanho = int(input('What would be the password size?: '))
        break
    except:
        print('Please input a valid number...')

letras = input('Would you like numbers? [Y/N]: ').strip().upper()
pontuações = input('Would you like punctuation? [Y/N]: ').strip().upper()

if letras == 'N' and pontuações == 'N':
    def id_generator(size=tamanho, chars=string.digits):
        print(''.join(random.choice(chars) for _ in range(size)))
    id_generator()

if letras == 'Y' and pontuações == 'N':
    def id_generator(size=tamanho, chars=string.ascii_uppercase + string.digits):
        print('Your password is: ' + ''.join(random.choice(chars) for _ in range(size)))
    id_generator()

if letras == 'N' and pontuações == 'Y':
    def id_generator(size=tamanho, chars=string.digits + string.punctuation):
        print('Your password is: ' + ''.join(random.choice(chars) for _ in range(size)))
    id_generator()

if letras == 'Y' and pontuações == 'Y':
    def id_generator(size=tamanho, chars=string.ascii_uppercase + string.digits + string.punctuation):
        print('Your password is: ' + ''.join(random.choice(chars) for _ in range(size)))
    id_generator()