from math import ceil

metrosParaPintar = float(input("Quantos metros quadrados precisa pintar: "))
litros_lata = 18
coberturaTinta = 3
latasNecessarias = metrosParaPintar / coberturaTinta / litros_lata

print("A quantidade de latas de tintas que precisa para pintar", metrosParaPintar, "metros", 
"são", ceil(latasNecessarias), "latas.")


