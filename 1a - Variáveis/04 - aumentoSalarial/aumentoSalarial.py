print("Aumento Salarial")

salario = float(input("Informe o valor de seu salário: "))
percentual_aumento = float(input("Informe o percentual de aumento: "))
valor_aumento = salario * percentual_aumento / 100
novo_salario = salario + valor_aumento

print("O seu novo salário será", novo_salario)
