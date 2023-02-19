#Leia o salario de um trabalhador e o valor da prestação de um emprestimo. 
#Se a prestação for mais de 20% do emprestimo imprima: Emprestimo não concedido, caso contrario. Emprestimo concedido

#Leia o salario
salario = float(input("Digite o salário: "))

#Leia valor da prestação do emprestimo
emprestimo = float(input("Digite a prestação do emprestimo: "))

#Verificando se a prestação vale mais que 20% do salario. 
parcela = (emprestimo * 100)/salario
if parcela > 20:
    print("Emprestimo não concedido!")
else:
    print("Emprestimo concedido!")