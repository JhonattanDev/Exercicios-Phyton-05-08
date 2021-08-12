# Explicando o programa
print("=================================================================")
print("|Digite o valor do salário para aplicar um aumento de 15% a ele!|")
print("=================================================================")

# Pedir ao Usuário inserir o valor do salário
salarioIncial = int(input("Digite o valor do salário: "))

# Cálculo
salarioComAcrescimo = salarioIncial * 1.15

# Imprimir, mostrar o resultado do programa
# {:.2f} para mostrar 2 número após o ponto
print("O valor original do salário era de R${:.2f}.".format(salarioIncial))
print("O valor do salário com acréscimo de 15% fica: R${:.2f}.".format(salarioComAcrescimo))
