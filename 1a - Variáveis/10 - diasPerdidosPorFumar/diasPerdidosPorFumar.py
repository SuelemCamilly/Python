cigarrosFumadosPorDia = int(input("Cigarros fumados por dia: "))
anosEmQueFumou = int(input("Quantidade de anos em que fumou: "))

diasEmUmAno = 365
diasTotaisEmQueFumou = anosEmQueFumou * diasEmUmAno

cigarrosTotaisFumadosNaVida = cigarrosFumadosPorDia * diasTotaisEmQueFumou 

minutosPerdidosPorCigarro = 10 
minutosPerdidosNaVida = cigarrosTotaisFumadosNaVida * minutosPerdidosPorCigarro

minutosEmUmaHora = 60
horasEmUmDia = 24
diasPerdidosnaVida = minutosPerdidosNaVida / minutosEmUmaHora / horasEmUmDia

print("Você perdeu", int(diasPerdidosnaVida), "dias de vida por ter fumado.")