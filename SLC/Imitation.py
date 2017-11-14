import random

def Imitation(winner, league_main, fitness_main, settings):

    nmain = settings['nmain']

    tau = random.uniform(0.2, 0.8)
    player1 = random.randint(0, nmain-1)
    player2 = random.randint(0, nmain-1)

    new_player = league_main[winner][0] + tau*(league_main[0][0] - league_main[winner][player1])
    print (new_player)
    print (league_main[winner][0])
