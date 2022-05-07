numero_inteiro = int(input("Digite um número inteiro menor que 1000: "))

unidade = numero_inteiro % 10
numero = (numero_inteiro - unidade) / 10
dezena = numero % 10
numero = (numero - dezena) / 10
centena = numero

print("O número", numero_inteiro, "tem", int(centena), "centenas,", int(dezena), "dezenas e", unidade, "unidades.")