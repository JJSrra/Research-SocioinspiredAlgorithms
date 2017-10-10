import numpy as np
from TestFoo import *

def CreateInitialLeague(settings):
    nteams = settings['nteams']
    nmain = settings['nmain']
    nsubs = settings['nsubs']
    dim = settings['dim']
    lower_bound = settings['lower_bound']
    upper_bound = settings['upper_bound']

    # League is splitted into two matrices, representing main and subs players of each team
    league_main = np.random.uniform(lower_bound,upper_bound,nteams*nmain*dim).reshape(nteams,nmain,dim)
    league_subs = np.random.uniform(lower_bound,upper_bound,nteams*nsubs*dim).reshape(nteams,nsubs,dim)

    # Fitness arrays
    #print (TestFoo(league_main[0][0]))
    fitness_main = np.ones(nteams*nmain)
    fitness_subs = np.ones(nteams*nsubs)

    # TODO assign correct values to fitness arrays

    # Now the 'Takhsis' is called for having the players sorted according to their fitness
