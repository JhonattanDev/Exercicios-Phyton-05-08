# Explicando o programa
print("============================================================")
print("|Digite o valor do produto para aplicá-lo o desconto de 5%!|")
print("============================================================")

# Pedir ao Usuário inserir o valor do produto
valorIncial = int(input("Digite o valor original do produto: "))

# Cálculo
valorDescontado = valorIncial * 0.95

# Imprimir, mostrar o resultado do programa
# {:.2f} para mostrar 2 número após o ponto
print("O valor original do produto era de R${:.2f}.".format(valorIncial))
print("O valor do produto com desconto de 5% fica R${:.2f}.".format(valorDescontado))