# Explicando o programa
print("==============================================")
print("|Calcule quanto será pago pelo carro alugado!|")
print("|    R$60 por dia e R$0,15 por Km rodado!    |")
print("==============================================")

# Pedir ao Usuário inserir os valores
diasAlugados = int(input("Insira aqui por quantos dias o carro foi utilizado: "))
kmRodados = int(input("Insira aqui quantos quilômetros (km) foram rodados: "))

# Cálculo dos valores
valorTotalDias = diasAlugados * 60
valorTotalKm = kmRodados * 0.15

# Cálculo do total a se pagar
totalAPagar = valorTotalDias + valorTotalKm

# Imprimir, mostrar o resultado do programa
print("==============================================")
print("O carro foi alugado por {} e rodou {} quilômetro(s).".format(diasAlugados, kmRodados))
print("Sendo assim, o total a ser pago pelo aluguel do carro é de: R${:.2f}".format(totalAPagar))