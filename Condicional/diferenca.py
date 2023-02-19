#Faça um programa que dado dois números. 
#Veja qual o maior e a diferença entre eles.

#Recebendo os números.

numeroA = int(input("Digite o primeiro número inteiro: "))

numeroB = int(input("Digite o segundo número inteiro: "))

#Verificando o maior entre eles e a diferença.

if numeroA > numeroB:
    print("O maior número é: {}, e a diferença entre os dois é de: {}".format(numeroA,(numeroA-numeroB)))
else: 
    print("Numero {} é o maior! E a diferença entre eles é de {}".format(numeroB, (numeroB-numeroA)))
    



