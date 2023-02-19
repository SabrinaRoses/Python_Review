#Leia um número escrito pelo o usuário se o número for positivo, calcule a raiz quadrada.
#Se o número for negativo, mostre uma mensagem dizendo que o número é invalido.

#Recebendo entrada do usuário
numero = float(input("Digite um número: "))

if numero > 0:
    raiz = numero ** (1/2)
    print("A raiz quadrada do número é: {:.2f}".format(raiz))
else:
    print("Este número é inválido")