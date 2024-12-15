# Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.

numero1 = int(input('Escreva um número de 1 a 100: '))
numero2 = int(input('Escreva outro número de 1 a 100: '))

if numero1 > numero2:
  print(f'O maior número é o {numero1}')

else:
  print(f'O maior número é o {numero2}')
