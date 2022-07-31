num = int(input('digite um número interio:'))
print('''Escolha uma das bases a seguir:
[ 1 ] Binário
[ 2 ] hexadecimal
[ 3 ] octal''')
op = int(input('Opção escolhida:'))
if op == 1:
    print('o número digitado, em binário, é {}'.format(bin(num)[2:]))
elif op == 2:
    print('o número digitado, em Hexadecimal, é {}'.format(hex(num)[2:]))
elif op == 3:
    print('o número digitado, em octal, é {}'.format(oct(num)[2:]))
else:
    print('Operação inválida!')