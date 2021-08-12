# Explicando o programa
print("=================================================================================")
print("|Digite a altura e largura da parede para saber a quantidade de tinta necessária|")
print("=================================================================================")

# Pedir ao Usuário inserir a altura e largura da parede
altura = int(input("Digite a altura da parede em m²: "))
larg = int(input("Digite a largura da parede em m²: "))

# Cálculos
area = larg * altura  # Calcular a área da parede
tinta = area / 2  # Calcular a quantidade de tinta necessária

# Imprimir, mostrar o resultado do programa
print("Para pintar esta parede de {} m², você precisa de {} L de tinta!".format(area, tinta))