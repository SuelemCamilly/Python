dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

total_segundos = segundos + (minutos * 60) + (horas * 60 * 60) + (dias * 24 * 60 * 60)

print(dias, " dias ", horas, " horas ", minutos, " minutos ", segundos, 
" segundos ", "= ", total_segundos, " segundos")