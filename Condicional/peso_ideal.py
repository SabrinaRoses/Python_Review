#Faça um programa que receba o sexo e a altura de uma pessoa. 
#calcule e mostre seu peso ideal.
#Homens (72.7 * h)-58 / Mulheres(62.1 * h)-44.7

#Recebendo a altura
h = float(input("Digite sua altura: "))

#Sexo
sexo = input("Digite 'F' para feminino ou 'M' para Masculino: ")
sexo = sexo.upper()

#Peso ideal
if sexo == 'F':
    pesoF = (62.1 * h) - 44.7
    print("O peso ideal é: {:.2f}".format(pesoF))
elif sexo == 'M':
    pesoM = (72.7 * h) - 58
    print("O peso ideal é: {:.2f}".format(pesoM))
else:
    print("Sexo inválido!")