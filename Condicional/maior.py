#Faça um programa que mostre qual dos dois números é o maior

#Receba o número

numeroA = int(input("Digite o primeiro número a ser comparado:\n"))
numeroB = int(input("Digite o segundo número a ser comparado:\n"))

#Comparar número

if numeroA > numeroB:
    print("O maior número é:", numeroA)
elif numeroB > numeroA:
    print("O maior número é:", numeroB)