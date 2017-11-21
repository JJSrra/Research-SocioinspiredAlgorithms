import numpy as np
from ProbabilityHost import *
from Imitation import *
from Provocation import *

def Competition(CostFunction,league_main,league_subs,fitness_main,fitness_subs,domain):

    nteams = league_main.shape[0]
    evals_competition = 0

    for i in range(0,nteams-2):
        for j in range(i+1,nteams):
            winner,loser = ProbabilityHost(i,j,league_main,fitness_main)
            league_main,fitness_main,evals_competition = Imitation(CostFunction,
                        winner,league_main,fitness_main,domain,evals_competition)
            league_subs,fitness_subs,evals_competition = Provocation(CostFunction,
                        winner,league_main,league_subs,fitness_subs,domain,evals_competition)

    return league_main,league_subs,fitness_main,fitness_subs,evals_competition
