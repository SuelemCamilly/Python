nota_prova1 = float(input("Nota da prova 1: "))
nota_exercicio1 = float(input("Nota do exercício 1: "))

nota_prova2 = float(input("Nota da prova 2: "))
nota_exercicio2 = float(input("Nota do exercício 2: "))

peso_prova = 7
peso_exercicio = 3

parcial1 = (nota_prova1 * 7 + nota_exercicio1 * 3) / (peso_prova + peso_exercicio)
parcial2 = (nota_prova2 * 7 + nota_exercicio2 * 3) / (peso_prova + peso_exercicio)

media = (parcial1 + parcial2) / 2

print("A média final é", int(media))

if media >= 7:
    print("Aprovado")

else: 
    print("Reprovado")


