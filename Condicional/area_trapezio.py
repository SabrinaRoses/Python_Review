#Faça um programa que calcule e mostre a área do trapezio.
#(Area BaseMaior + BaseMenor )* Altura /2


#Leia areas
baseA = float(input("Digite a Base Maior: "))
baseB = float(input("Digite a Base Menor: "))
altura = float(input("Digite a altura: "))

#Calcule área
area = ((baseA + baseB) * altura) / 2

#Mostrando Area do trapezio:
print("A area do trapezio de Base Maior {}, e Base Menor {}, com altura de {:.2f}. É: {:.2f}".format(baseA, baseB, altura, area))
