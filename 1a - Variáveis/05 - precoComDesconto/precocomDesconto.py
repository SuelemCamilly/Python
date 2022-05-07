preco_original = float(input("Informe o valor original do produto: "))
porcentagem_desconto = float(input("Informe o desconto: "))
valor_desconto = preco_original * porcentagem_desconto/100
precoDesconto = preco_original - valor_desconto

print("O preço com desconto é ", precoDesconto)

