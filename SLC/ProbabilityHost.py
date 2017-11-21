import numpy as np
import random

def ProbabilityHost(i, j, league_main, fitness_main):

    icost = np.mean(fitness_main[i])
    jcost = np.mean(fitness_main[j])

    phost = icost/(icost+jcost)
    rand = random.uniform(0,1)

    if rand>phost:
        winner = i
        loser = j
    else:
        winner = j
        loser = i

    return winner, loser
