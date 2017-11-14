import numpy as np
from ProbabilityHost import *
from Imitation import *

def Competition(league_main, league_subs, fitness_main, fitness_subs, settings):

    nteams = settings['nteams']

    for i in range(0,nteams-2):
        for j in range(i+1,nteams):
            print (i, j)
            winner, loser = ProbabilityHost(i,j,league_main,fitness_main)
            Imitation(winner, league_main, fitness_main, settings)
            #Provocation(winner, league_subs, fitness_subs, settings)
