#Faça um programa que mostre o usuário um menu com 4 opções de operações matematicas.
#O usuário escolhe uma das opções e o programa então pede 2 números e realiza a operação mostrando o resultado.


#Pedindo o usuário para que escolha o tipo de operaçao
op = int(input("Digite a operação desejada: \n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n\n"))

#Solicitando dois números de entrada:
num1 = int(input("Escolha dois números: "))
num2 = float(input())

#Montando a operação de acordo com  a escolha do usuário
if op == 1:
    print("A soma dos valores é: {}".format(num1+num2))
elif op == 2:
    print("A subtração dos valores é: {}".format(num1-num2))
elif op == 3:
    print("A multiplicação dos valores é: {}".format(num1*num2))
elif op == 4:
    print("A visão dos dois valores é: {}".format(num1/num2))
