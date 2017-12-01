import numpy as np
import math

def LoserFunction(CostFunction, loser, league_main, fitness_main, league_subs, fitness_subs, mutation_rate, mutation_probability, domain, evals_competition):

    nmain,dim = league_main.shape[1:]

    players_selected = np.random.permutation(np.arange(nmain))[0:3]

    num_mutations = math.ceil(mutation_probability*dim)
    mutations = np.random.permutation(np.arange(dim))[0:num_mutations]

    
