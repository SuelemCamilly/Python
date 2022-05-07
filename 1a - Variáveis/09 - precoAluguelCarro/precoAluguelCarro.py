dias = float(input("Informe quantos dias o carro foi alugado: "))
km_rodados = float(input("Informe a quantidade de km rodados: "))

preco_aluguel = (dias * 60) + (km_rodados * 15/100)

print("O preço do aluguel do carro ficou R$", preco_aluguel)