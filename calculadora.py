#calculadora em python

print("=== CALCULADORA ===")

num1 = int(input('Digita primeiro numero: '))

num2 = int(input('Digita segundo numero: '))

operador = input('Digita o operador (+, -, *, /): ')

if operador == '+' :
    soma = num1 + num2
    print('Resultado da soma = {}'.format(soma))

elif operador == '-' :
    sub = num1 - num2
    print('Resultado da subtração = {}'.format(sub))

elif operador == '*' :
    mult = num1 * num2
    print('Resultado da multiplicação = {}'.format(mult))

elif operador == '/' :
    if num2 == 0:
        print('Não possivel dividir por zero!')
    else :
        div = num1 / num2
        print('Resultado da divisão = {}'.format(div))

else :
    print('operador invalido!')