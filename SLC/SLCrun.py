# Soccer League Competition Algorithm (For Continuous Decision Variables)
# Developed By: Naser Moosavian
# Translated to Python By: Juanjo Sierra

import numpy as np
from CreateInitialLeague import *
from Competition import *
from Takhsis import *
from  TestFoo import *

if __name__ == "__main__":

    # Define Cost Funcion
    CostFunction = TestFoo

    # Define settings of the problem
    settings = {'max_eval': 50000, 'dim': 10, 'nteams': 5,
                'lower_bound': 0, 'upper_bound': 10, 'neval': 0, 'max_it': 10**8,
                'mutation_probability': 0.1, 'mutation_rate': 0.2}

    # Number of main and subs players are equal to the dimension of the problem,
    # although this may change
    settings['nmain'] = settings['dim']
    settings['nsubs'] = settings['dim']

    # Domain of the problem, tuple including lower and upper bounds
    domain = (settings['lower_bound'], settings['upper_bound'])

    # Creation of the initial league
    league_main,league_subs,fitness_main,fitness_subs = CreateInitialLeague(CostFunction, settings['nteams'],
                settings['nmain'], settings['nsubs'], settings['dim'], domain)

    # Seasons keep on launching until 'max_it' seasons have been played, or until 'neval' reaches number of Cost
    # Function evaluations that was indicated as a ceiling parameter
    for it in range(0,settings['max_it']):
        league_main,league_subs,fitness_main,fitness_subs,evals_competition = Competition(CostFunction,
                    league_main,league_subs,fitness_main,fitness_subs,domain)
        settings['neval'] += evals_competition
        league_main,league_subs,fitness_main,fitness_subs = Takhsis(league_main,league_subs,fitness_main,fitness_subs)

        print("Season {}, best solution: {:e}".format(it, fitness_main[0][0]))

        if (settings['neval'] > settings['max_eval']) or (fitness_main[0][0] == 0.0):
            break
