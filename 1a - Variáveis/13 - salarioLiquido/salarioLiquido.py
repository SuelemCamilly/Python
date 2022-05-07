valor_hora = float(input("Informe o valor recebido por hora trabalhada: "))
horas_trabalhadas = int(input("Informe as horas trabalhadas no mês: "))
salario_bruto = valor_hora * horas_trabalhadas

inss = salario_bruto * 8/100
ir = salario_bruto * 11/100
sind = salario_bruto * 5/100

salario_liquido = salario_bruto - (inss + ir + sind)

print("O valor do salário líquido é R$", salario_liquido)