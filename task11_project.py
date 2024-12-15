# Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. 
# O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais; Triângulo Isósceles: quaisquer dois lados iguais; Triângulo Escaleno: três lados diferentes.

print('''Vamos montar um triângulo!
Você informa os valores dos lados''')
print()
lado1 = int(input('Digite o valor do primeiro lado: '))
lado2 = int(input('Digite o valor do segundo lado: '))
lado3 = int(input('Digite o valor do terceiro lado: '))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
  print('Ok, vamos montar!')

  if lado1 == lado2 and lado2 == lado3:
    print('Com esses valores monta-se um triângulo equilátero.')

  if lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
    print('Com esses valores monta-se um triângulo isósceles.')

  elif lado1 != lado2 != lado3:
    print('Com esses valores podemos fazer um triângulo escaleno.')

else:
  print('Refaça o teste, pois com esses valores não se faz um triângulo.')
