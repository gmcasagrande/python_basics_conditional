# Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. 
# O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. 
# A partir do valor da variação, deve ser enviada às seguintes sugestões:
# Para variação acima de 20%: bonificação para o time de vendas.
# Para variação entre 2% e 20%: pequena bonificação para time de vendas.
# Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
# Para variação abaixo de -10%: corte de gastos.

v22 = int(input('Digite a quantidade de vendas de 2022: '))
v23 = int(input('Digite a quantidade de vendas de 2023: '))
variacao = v23 - v22

if variacao > float(v22 * 0.2):
  print('BONIFICAÇÃO PARA O TIME DE VENDAS!!')

elif float(v22 * 0.02) <= variacao < float(v22 * 0.2):
  print('Pequena bonificação para o time de vendas.')

elif float(v22 - (v22 * 1.1)) <= variacao <= float(v22 * 0.02):
  print('Planejamento de políticas de incentivo às vendas.')

else:
  print('Corte de gastos')
