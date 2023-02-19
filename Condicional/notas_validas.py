#faça um programa que leia duas notas de um aluno, verifique se as notas são validas e exiba na tela a média.
#Uma nota deve ser valida, obrigatoriamente um valor entre 0.0 e 10.0. Onde caso a nota náo possua um valor valido
#Mostre uma mensagem informando ao usuario e termine o programa.

#Recendo duas notas.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

#Verificador de notas validas

if nota1 < 0 or nota1 > 10:
    print("Esta nota é invalida. A nota deve ser maior ou igual a 0.0 ou menor ou igual a 10.0")
elif nota2 < 0 or nota2 >10:
    print("Esta nota é invalida. A nota deve ser maior ou igual a 0.0 ou menor ou igual a 10.0")
else:
    media = (nota1 + nota2) / 2
    print("A media do aluno é {:.2f}".format(media))
