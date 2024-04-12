#Saca el maximo recibiendo una lista de tuplas como parametro
def maximum(players):
    max = -1
    for player in players:
        if(player[1] > max):
            max = player[1]
            aux =(player[0],player[1])
    return aux

#Calcula la efectividad de l@s jugador@s
def effectiveness(data):
    aux = []
    for player in data:
        aux.append((player[0],(player[1] * 1.5) + (player[2] * 1.25) + player[3]))
    return aux

