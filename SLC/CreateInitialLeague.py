import numpy as np
from Takhsis import *

def CreateInitialLeague(CostFunction, nteams, nmain, nsubs, dim, domain, initial_domain):
    lower_bound, upper_bound = domain
    initial_lower_bound, initial_upper_bound = initial_domain

    if initial_lower_bound != None and initial_upper_bound != None:
        lower_bound = initial_lower_bound
        upper_bound = initial_upper_bound

    # League is splitted into two matrices, representing main and subs players of each team
    league_main = np.random.uniform(lower_bound,upper_bound,nteams*nmain*dim).reshape(nteams,nmain,dim)
    league_subs = np.random.uniform(lower_bound,upper_bound,nteams*nsubs*dim).reshape(nteams,nsubs,dim)

    # Fitness arrays
    fitness_main = np.apply_along_axis(CostFunction, 2, league_main)
    fitness_subs = np.apply_along_axis(CostFunction, 2, league_subs)
    initial_evals = nteams*nmain + nteams*nsubs

    # Now the 'Takhsis' is called for having the players sorted according to their fitness
    league_main,league_subs,fitness_main,fitness_subs = Takhsis(league_main, league_subs, fitness_main, fitness_subs)

    return league_main,league_subs,fitness_main,fitness_subs,initial_evals
