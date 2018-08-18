# Soccer League Competition Algorithm (For Continuous Decision Variables)
# Developed By: Naser Moosavian
# Translated to Python By: Juanjo Sierra

import numpy as np
from CreateInitialLeague import *
from Competition import *
from Takhsis import *

def SLC(CostFunction, max_eval=50000, dim=30, nteams=5, nmain=10, nsubs=10, lower_bound=0,
        upper_bound=10, max_it=10**8, mutation_probability=0.1, mutation_rate=0.2):

    # Domain of the problem, tuple including lower and upper bounds
    domain = (lower_bound, upper_bound)

    # Creation of the initial league
    league_main,league_subs,fitness_main,fitness_subs,initial_evals = CreateInitialLeague(CostFunction,
                nteams, nmain, nsubs, dim, domain)

    # Starting number of evaluations
    neval = initial_evals

    # Seasons keep on launching until 'max_it' seasons have been played, or until 'neval' reaches number of Cost
    # Function evaluations that was indicated as a ceiling parameter
    for it in range(0,max_it):
        league_main,league_subs,fitness_main,fitness_subs,evals_competition = Competition(CostFunction,
                    league_main,league_subs,fitness_main,fitness_subs,domain,mutation_rate,mutation_probability)
        neval += evals_competition
        league_main,league_subs,fitness_main,fitness_subs = Takhsis(league_main,league_subs,fitness_main,fitness_subs)

        # print("Season {:4}, best solution: {:e}".format(it, fitness_main[0][0]))
        # print("\tNumber of evaluations: {}".format(neval))

        if neval > max_eval:
            break

    return fitness_main[0][0]
