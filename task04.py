# Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.

preco2021 = float(input('Digite o valor do carro em 2021: '))
preco2022 = float(input('Digite o valor do carro em 2022: '))
preco2023 = float(input('Digite o valor do carro em 2023: '))
print()

#inicio o if com o valor de 2021 mais alto:
if preco2021 > preco2022 and preco2021 > preco2023:

  if preco2022 > preco2023:
    print('O maior valor foi de R$%.2f, do ano 2021.' %(preco2021))
    print('O menor valor foi de R$%.2f, do ano 2023.' %(preco2023))
  else:
    print('O maior valor foi de R$%.2f, do ano 2021.' %(preco2021))
    print('O menor valor foi de R$%.2f, do ano 2022.' %(preco2022))

# este elif indicará o valor de 2022 como o mais alto:
elif preco2022 > preco2021 and preco2022 > preco2023:

  if preco2021 > preco2023:
    print('O maior valor foi de R$%.2f, do ano 2022.' %(preco2022))
    print('O menor valor foi de R$%.2f, do ano 2023.' %(preco2023))
  else:
    print('O maior valor foi de R$%.2f, do ano 2022.' %(preco2022))
    print('O menor valor foi de R$%.2f, do ano 2021.' %(preco2021))

# aqui termino indicando que o valor de 2023 será o mais alto:
elif preco2023 > preco2021 and preco2023 > preco2022:

  if preco2021 > preco2022:
    print('O maior valor foi de R$%.2f, do ano 2023.' %(preco2023))
    print('O menor valor foi de R$%.2f, do ano 2022.' %(preco2022))
  else:
    print('O maior valor foi de R$%.2f, do ano 2023.' %(preco2023))
    print('O menor valor foi de R$%.2f, do ano 2021.' %(preco2021))
