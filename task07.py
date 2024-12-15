# Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.

turno = str(input('Qual turno você estuda? Resposta: ')).upper()

if turno == 'MANHÃ' or 'MANHA':
  print('Bom Dia!')

elif turno == 'TARDE':
  print('Boa Tarde!')

elif turno == 'NOITE':
  print('Boa Noite!')

else:
  print('Valor inválido!')
