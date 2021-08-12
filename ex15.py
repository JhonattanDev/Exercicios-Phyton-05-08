# Explicando o programa
print("==============================================================================")
print("|Digite a temperatura em Graus Celsius (ºC) para converter em Fahrenheit (ºF)|")
print("==============================================================================")

# Pedir ao Usuário inserir o valor da temperatura em graus Celsius
grausCelsius = int(input("Digite a temperatura em Graus Celsius (ºC): "))

# Cálculo
grausEmFahrenheit = ((9 * grausCelsius) / 5) + 32

# Imprimir, mostrar o resultado do programa
print("- {}ºC (Graus Celsius) correspondem à {:.1f}ºF (Graus Fahrenheit).".format(grausCelsius, grausEmFahrenheit))
