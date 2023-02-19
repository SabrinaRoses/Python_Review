#Ler um número inteiro, se o número for negativo. Poste número invalido. 
#Se for positivo, calcule o logaritmo.

import math

#Lendo o número
numero = int(input("Digite um número: "))

#Verificando se o número é válido
if numero <0:
    print("Número inválido!")
else:
#Calcule logaritmo.
   logaritmo = math.log(numero)

print(logaritmo)
