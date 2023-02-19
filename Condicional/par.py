#Faça um programa que receba um número inteiro
#Mostre se o número é par ou impar.

#Recebendo o número

numero = int(input("Digite um número: "))

#Comparador par

if numero%2 == 0:
    print("Este número é par.")
else: 
    print("Este número é impar.")