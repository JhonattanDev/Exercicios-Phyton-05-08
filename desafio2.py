import random

# Explicando o programa
print("================================")
print("|      Gerador de Boletos      |")
print("================================")

# Onde o programa vai pedir ao usuário inserir os valores
agencia = input("Insaria aqui o número do seu banco (Exemplo: 341-7): ")
numeroAleatorio = random.randrange(1000, 10000)  # Deixei gerar até 9999, para continuar na casa dos 4341 dígitos
dia = input("Insira o dia aqui (Exemplo: Dia 02 = 02): ")
mes = input("Insira o mês aqui (Exemplo: Mês de Setembro = 09): ")
ano = input("Insira o ano aqui (Exemplo: Ano de 2021 = 2021): ")
oitoZeros = "00000000"
valorDoBoleto = input("Insira o valor do seu boleto abaixo (Exemplo: R$399,90 = 39990) \n")

# Imprimir/mostrar o resultado do programa
print("{} | {}{}{}{}{}{}".format(agencia, numeroAleatorio, dia, mes, ano, oitoZeros, valorDoBoleto))