# Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.

num = float(input('Digite um número (use ponto. para n° fracionado): '))

if num == 0:
  num = int(num)
  print(f'O número {num} é inteiro.')
else:
  if num % 1 == 0:
    num = int(num)
    print(f'O número {num} é inteiro.')
  else:
    print(f'O número {num} é decimal.')
