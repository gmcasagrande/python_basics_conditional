# Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).

janeiro = int(input('Digite a produção de janeiro: '))
dezembro = int(input('Digite a produção de dezembro: '))

if janeiro > dezembro:
  print(f'De janeiro a dezembro houve declínio da produção.')

else:
  print(f'De janeiro a dezembro houve aumento da produção.')
