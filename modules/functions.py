def goals_maximun(players):
    maximun = -1
    aux = None
    for player in players:
        if(player[1] > maximun):
            maximun = player[1]
            aux =(player[0],player[1])
    return aux

