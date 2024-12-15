# Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.

vogais = 'A, E, I, O, U'
letra = str(input('Digite uma letra: ')).upper()

if letra in vogais:
  print(f'A letra "{letra}" é uma vogal')

else:
  print(f'A letra "{letra}" é uma consoante')
