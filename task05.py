# Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.

banana = float(input('Digite o preço da banana: '))
laranja = float(input('Digite o preço da laranja: '))
uva = float(input('Digite o preço da uva: '))

if banana < laranja and banana < uva:
  print(f'O produto mais barato é a banana.')

elif laranja < banana and laranja < uva:
  print('A laranja está mais barata.')

elif uva < banana and uva < laranja:
  print('Compre uvas, estão mais baratas.')
