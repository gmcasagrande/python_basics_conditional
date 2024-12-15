# Escreva um programa que leia três números e os exiba em ordem decrescente.

num1 = int(input('Digite um número de 1 a 100: '))
num2 = int(input('Digite outro número de 1 a 100: '))
num3 = int(input('Digite outro número de 1 a 100: '))

if num1 > num2 and num1 > num3:
  if num2 > num3:
    print(f'A ordem decrescente dos números é {num1}, {num2} e {num3}.')
  else:
    print(f'A ordem decrescente dos números é {num1}, {num3} e {num2}.')

elif num2 > num1 and num2 > num3:
  if num1 > num3:
    print(f'A ordem decrescente dos números é {num2}, {num1}, e {num3}.')
  else:
    print(f'A ordem decrescente dos números é {num2}, {num3}, e {num1}.')

elif num3 > num1 and num3 > num2:
  if num1 > num2:
    print(f'A ordem decrescente dos números é {num3}, {num1}, e {num2}.')
  else:
    print(f'A ordem decrescente dos números é {num3}, {num2}, e {num1}.')
