# Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. 
# O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

(print('''O programa irá te solicitar dois números.
Você tem liberdade para escolher qualquer número, seja inteiro, fracionado, positivo, negativo...
Depois irá pedir um número de 1 a 4, que represente um operador matemático.
Vamos lá!!'''))
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
operador = int(input('''Escolha uma opção de 1 a 4:
1: Adição 
2: Subtração 
3: Multiplicação 
4: Divisão 
Resposta: '''))
print()

if operador == 1:
  soma = numero1 + numero2
  print(f'A operação é adição: {numero1} + {numero2} = {soma}')
  restoSoma = soma % 2
  if restoSoma >= 1:
    print(f'O número {soma} é ímpar.')
  else:
    print(f'O número {soma} é par.')
  if type(soma) is float:
    print(f'O número {soma} é decimal.')
  else:
    print(f'O número {soma} é inteiro.')
  if soma < 0:
    print(f'O número {soma} é negativo.')
  else:
    print(f'O número {soma} é positivo.')


elif operador == 2:
  sub = numero1 - numero2
  print(f'A operação é subtração: {numero1} - {numero2} = {sub}')
  restoSub = sub % 2
  if restoSub >= 1:
    print(f'O número {sub} é ímpar.')
  else:
    print(f'O número {sub} é par.')
  if type(sub) is float:
    print(f'O número {sub} é decimal.')
  else:
    print(f'O número {sub} é inteiro.')
  if sub < 0:
    print(f'O número {sub} é negativo.')
  else:
    print(f'O número {sub} é positivo.')


elif operador == 3:
  mult = numero1 * numero2
  print(f'A operação é multiplicação: {numero1} * {numero2} = {mult}')
  restoMult = mult % 2
  if restoMult >= 1:
    print(f'O número {mult} é ímpar.')
  else:
    print(f'O número {mult} é par.')
  if type(mult) is float:
    print(f'O número {mult} é decimal.')
  else:
    print(f'O número {mult} é inteiro.')
  if mult < 0:
    print(f'O número {mult} é negativo.')
  else:
    print(f'O número {mult} é positivo.')

elif operador == 4:
  div = numero1 / numero2
  print(f'A operação é divisão: {numero1} / {numero2} = {div:.2f}')
  restoDiv = div % 2
  if restoDiv >= 1:
    print(f'O número {div:.2f} é ímpar.')
  else:
    print(f'O número {div:.2f} é par.')
  if type(div) is float:
    print(f'O número {div:.2f} é decimal.')
  else:
    print(f'O número {div:.2f} é inteiro.')
  if div < 0:
    print(f'O número {div:.2f} é negativo.')
  else:
    print(f'O número {div:.2f} é positivo.')
