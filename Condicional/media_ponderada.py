#Faça um programa que calcule a media ponderada nas notas de 3 provas.
#A primeira e a segunda prova tem peso 1, a terceira tem peso 2.
#Ao final indicar a media e mostrar se o aluno foi aprovado ou reprovado (Aprovado, supeior a 60 pontos)

#Recebendo as notas.
Nota1 = float(input("Digite a primeira nota: "))
Nota2 = float(input("Digite a segunda nota: "))
Nota3 = float(input("Digite a terceira nota: "))

#Calculando Média
media = (Nota1 + Nota2 + (Nota3*2))/3

#Mostrando se o aluno foi aprovado
if media >= 6.0:
    print("Aluno aprovado! Média {:.2f}".format(media))
else:
    print("Aluno reprovado! Média inferior a 60.\n Média do Aluno: {:.2f}".format(media))