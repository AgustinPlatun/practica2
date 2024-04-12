#Saca el maximo recibiendo una lista de tuplas como parametro
def maximum(players):
    max = -1
    for player in players:
        if(player[1] > max):
            max = player[1]
            aux =(player[0],player[1])
    return aux

#Calcula el total de goles
def average_matches(data):
    aux = 0
    for player in data:
        aux += player[1]
    return aux

