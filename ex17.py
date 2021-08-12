import random

# Explicando o programa
print("=============================================")
print("|Digite o nome de 4 alunos para sortear-los!|")
print("=============================================")

# Pedir ao Usuário inserir os nomes dos alunos
aluno1 = input("Insira o nome do primeiro aluno: ")
aluno2 = input("Insira o nome do segundo aluno: ")
aluno3 = input("Insira o nome do terceiro aluno: ")
aluno4 = input("Insira o nome do quarto aluno: ")

# Sortear um número de 1 a 4
numeroSorteado = random.randrange(1, 5)

# Imprimir/mostrar o resultado do programa
print("=============================================")

# Comparar o número sorteado pelo random.randrange com qual aluno será escolhido
if(numeroSorteado == 1):
    print("O aluno escolhido foi {}.".format(aluno1))
elif(numeroSorteado == 2):
    print("O aluno escolhido foi {}.".format(aluno2))
elif(numeroSorteado == 3):
    print("O aluno escolhido foi {}.".format(aluno3))
else:  # Ou também pode ser utilizado o termo: elif(numeroSorteado == 4):
    print("O aluno escolhido foi {}.".format(aluno4))
