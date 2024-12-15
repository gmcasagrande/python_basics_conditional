# Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.

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
