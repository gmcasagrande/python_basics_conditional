# Um estabelecimento está vendendo combustíveis com descontos variados. 
# Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. 
# Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. 
# O preço do litro de diesel é R$2,00 e o preço do litro de etanol é R$1,70. 

# Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:
# O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
# O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.

print('''
Seja bem vindo(a) ao posto de abastecimento.
Valores dos combustíveis:
ETANOL R$1,70 
DIESEL R$ 2,00

PROMOÇÃO!! Desconto de 2% no Etanol e de 3% no Diesel.
E tem mais! Abastecendo a partir de 15 litros...
...seu desconto será de 4% no Etanol...
...ou de 5% no Diesel!
Aproveite!!
''')
combustivel = str(input('''Digite a letra do combustível desejado:
E para Etanol ou D para Diesel.
Resposta:  ''')).upper()
litros = float(input('Digite a quantidade de litros desejada: '))
precoE = 1.70 # valor do litro do etanol
precoD = 2.00 # valor do litro do diesel


if combustivel == 'E':
  print('O combustível escolhido foi o Etanol.')
  if litros <= 15:
    desconto = 2
    desconto2 = float(desconto / 100)
    valorDesconto = precoE * litros * desconto2
    valor = litros * precoE - valorDesconto
    print(f'''
    Seu desconto será de {desconto}% por litro.
    O total de desconto foi de R${valorDesconto}
    O total a pagar foi de R${valor}''')
  else:
    desconto = 4
    desconto2 = float(desconto / 100)
    valorDesconto = precoE * litros * desconto2
    valor = litros * precoE - valorDesconto
    print(f'''
    Seu desconto será de {desconto}% por litro.
    O total de desconto foi de R${valorDesconto}
    O total a pagar foi de R${valor}''')

if combustivel == 'D':
  print('O combustível escolhido foi o Diesel.')
  if litros <= 15:
    desconto = 3
    desconto2 = float(desconto / 100)
    valorDesconto = precoE * litros * desconto2
    valor = litros * precoE - valorDesconto
    print(f'''
    Seu desconto será de {desconto}% por litro.
    O total de desconto foi de R${valorDesconto}
    O total a pagar foi de R${valor}''')
  else:
    desconto = 5
    desconto2 = float(desconto / 100)
    valorDesconto = precoE * litros * desconto2
    valor = litros * precoE - valorDesconto
    print(f'''Seu desconto será de {desconto}% por litro.
    O total de desconto foi de R${valorDesconto}
    O total a pagar foi de R${valor}''')
