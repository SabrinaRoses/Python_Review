#Escreva um programa que leia um número inteiro maior do que zero
#E faça a soma de todos os algarismos. 

#Leia número inteiro:
numero = int(input("Digite um número inteiro: "))

#Decompor número.

#Passando número para string.

texto = str(numero)
soma = 0

#Laço para ler cada string na posição x e somar o valor
for value in texto:
    soma = soma + int(value)
print(soma)


