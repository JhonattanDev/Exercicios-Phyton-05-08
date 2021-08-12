import random

# Explicando o programa
print("==================================")
print("|       SISTEMA FINANCEIRO       |")
print("==================================")

# Pedindo ao usuário inserir o nome do funcionário e de quanto será seu salário
funcionario1 = input("Digite o nome do funcionário: ")
salario1 = int(input("Insira o salário deste funcionário: R$"))

funcionario2 = input("Digite o nome do funcionário: ")
salario2 = int(input("Insira o salário deste funcionário: R$"))

funcionario3 = input("Digite o nome do funcionário: ")
salario3 = int(input("Insira o salário deste funcionário: R$"))

# Calculando o aumento de 5% no salário
salario1 = salario1 * 1.05
salario2 = salario2 * 1.05
salario3 = salario3 * 1.05

funcionario4 = input("Digite o nome do funcionário: ")
salario4 = int(input("Insira o salário deste funcionário: R$"))

funcionario5 = input("Digite o nome do funcionário: ")
salario5 = int(input("Insira o salário deste funcionário: R$"))

funcionario6 = input("Digite o nome do funcionário: ")
salario6 = int(input("Insira o salário deste funcionário: R$"))

# Calculando o aumento de 5% no salário
salario1 = salario1 * 1.05
salario2 = salario2 * 1.05
salario3 = salario3 * 1.05
salario4 = salario4 * 1.05
salario5 = salario5 * 1.05
salario6 = salario6 * 1.05

funcionario7 = input("Digite o nome do funcionário: ")
salario7 = int(input("Insira o salário deste funcionário: R$"))

funcionario8 = input("Digite o nome do funcionário: ")
salario8 = int(input("Insira o salário deste funcionário: R$"))

funcionario9 = input("Digite o nome do funcionário: ")
salario9 = int(input("Insira o salário deste funcionário: R$"))

# Calculando o aumento de 5% no salário
salario1 = salario1 * 1.05
salario2 = salario2 * 1.05
salario3 = salario3 * 1.05
salario4 = salario4 * 1.05
salario5 = salario5 * 1.05
salario6 = salario6 * 1.05
salario7 = salario7 * 1.05
salario8 = salario8 * 1.05
salario9 = salario9 * 1.05

funcionario10 = input("Digite o nome do funcionário: ")
salario10 = int(input("Insira o salário deste funcionário: R$"))

# SORTEIO
# Sorteando um número aleatório (1 a 10)
numeroSorteado = random.randrange(1, 11)

# Comparando quem vai ser o premiado
if(numeroSorteado == 1):
    salario1 = salario1 * 1.10  # Acréscimo de 10% no seu sálario
    funcionarioSorteado = funcionario1
elif(numeroSorteado == 2):
    salario2 = salario2 * 1.10  # Acréscimo de 10% no seu sálario
    funcionarioSorteado = funcionario2
elif(numeroSorteado == 3):
    salario3 = salario3 * 1.10  # Acréscimo de 10% no seu sálario
    funcionarioSorteado = funcionario3
elif(numeroSorteado == 4):
    salario4 = salario4 * 1.10  # Acréscimo de 10% no seu sálario
    funcionarioSorteado = funcionario4
elif(numeroSorteado == 5):
    salario5 = salario5 * 1.10  # Acréscimo de 10% no seu sálario
    funcionarioSorteado = funcionario5
elif(numeroSorteado == 6):
    salario6 = salario6 * 1.10  # Acréscimo de 10% no seu sálario
    funcionarioSorteado = funcionario6
elif(numeroSorteado == 7):
    salario7 = salario7 * 1.10  # Acréscimo de 10% no seu sálario
    funcionarioSorteado = funcionario7
elif(numeroSorteado == 8):
    salario8 = salario8 * 1.10  # Acréscimo de 10% no seu sálario
    funcionarioSorteado = funcionario8
elif(numeroSorteado == 9):
    salario9 = salario9 * 1.10  # Acréscimo de 10% no seu sálario
    funcionarioSorteado = funcionario9
else:  # elif(numeroSorteado == 10):
    salario10 = salario10 * 1.10  # Acréscimo de 10% no seu sálario
    funcionarioSorteado = funcionario10

# Programa para e imprime o resultado

# Imprimir/mostrar o resultado do código
print("==================================")
print("Funcionário {}, salário de R${:.2f}.".format(funcionario1, salario1))
print("Funcionário {}, salário de R${:.2f}.".format(funcionario2, salario2))
print("Funcionário {}, salário de R${:.2f}.".format(funcionario3, salario3))
print("Funcionário {}, salário de R${:.2f}.".format(funcionario4, salario4))
print("Funcionário {}, salário de R${:.2f}.".format(funcionario5, salario5))
print("Funcionário {}, salário de R${:.2f}.".format(funcionario6, salario6))
print("Funcionário {}, salário de R${:.2f}.".format(funcionario7, salario7))
print("Funcionário {}, salário de R${:.2f}.".format(funcionario8, salario8))
print("Funcionário {}, salário de R${:.2f}.".format(funcionario9, salario9))
print("Funcionário {}, salário de R${:.2f}.".format(funcionario10, salario10))
print("==================================")
print("O funcionário premiado foi {}, recebendo um bônus de 10% em seu salário.".format(funcionarioSorteado))
