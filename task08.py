# Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.

numeroInteiro = int(input('Digite um número inteiro: '))

resto = numeroInteiro % 2

if resto >= 1:
  print(f'O número {numeroInteiro} é ímpar.')

else:
  print(f'O número {numeroInteiro} é par.')
