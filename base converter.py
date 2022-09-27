num = int(input('Type an integer: '))
print('''Choose one of the options bellow:
[ 1 ] Binary
[ 2 ] hexadecimal
[ 3 ] octal''')
op = int(input('Chosen option:'))
if op == 1:
    print('The typed number in binary is {}'.format(bin(num)[2:]))
elif op == 2:
    print('The typed number in hexadecimal is {}'.format(hex(num)[2:]))
elif op == 3:
    print('The typed number in octal is {}'.format(oct(num)[2:]))
else:
    print('invalid option!')
