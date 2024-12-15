# Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. 
# O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

# Nesta resolução, as resoluções foram desagrupadas, resultando em um código menor com a atribuição da variável genérica "operacao"

opcao = int(input('Escolha uma operação: \n1-Soma; \n2-Subtração; \n3-Multiplicação; \n4-Divisão; \n'))
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

# Aqui será definida a operação e seu resultado
if opcao == 1:
  soma = num1 + num2
  print(f'opcao: {opcao}\nSoma:{num1}+{num2}={soma}')
  operacao = soma
elif opcao == 2:
  subtracao = num1 - num2
  print(f'opcao: {opcao}\nSubtração:{num1}-{num2}={subtracao}')
  operacao = subtracao
elif opcao == 3:
  multiplicacao = num1 * num2
  print(f'opcao: {opcao}\nMultiplicação:{num1}*{num2}={multiplicacao}')
  operacao = multiplicacao
elif opcao == 4:
  divisao = num1 / num2
  print(f'opcao: {opcao}\nDivisão:{num1}/{num2}={divisao:.2f}')
  operacao = divisao
  operacao = float(operacao)
else:
  print('Opção inválida')

# A partir daqui, o código vai verificar as características da operação
resto = operacao % 2

if resto == 0:
  print('número par')
else:
  print('número ímpar')

if operacao > 0:
  print('número positivo')
else:
  print('número negativo')

resto1 = operacao % 1
if resto1 == 0:
  print('número inteiro')
else:
  print('número decimal')
