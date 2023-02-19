#Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário imprima o número ao quadrado.

#Lendo o numero real.

numero = float(input("Digite um número real: "))

#Comparador de número positivo. 

if numero > 0:
    #Imprima a raiza
    raiz = numero ** (1/2)
    print("A raiz quadrada é {:.2f}".format(raiz))
else:
    quadrado = numero **2
    print("O número elevado ao quadrado: {:.2f}".format(quadrado))