# Explicando o programa
print("====================================================")
print("|Digite o valor em R$ abaixo para converter para U$|")
print("====================================================")

# Usuário insirir o valor em reais
valorReais = int(input("Digite o valor em reais: "))

# Definindo o valor do dolar, no caso 5 e 30 centavos
dolar = 5.30

# Cálculo da conversão de reais em dólar
conversao = valorReais / dolar

# Imprimir, mostrar o resultado do programa
print("Com {} reais, você consegue comprar {:.2f} dólares!".format(valorReais, conversao))