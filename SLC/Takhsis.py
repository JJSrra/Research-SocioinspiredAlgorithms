import numpy as np
from TestFoo import *

def Takhsis(league_main, league_subs, fitness_main, fitness_subs, settings):

    nteams = settings['nteams']
    nmain = settings['nmain']
    nsubs = settings['nsubs']
    dim = settings['dim']

    league = np.append(league_main, league_subs, axis=0).reshape(nteams*(nmain+nsubs), dim)
    fitness = np.append(fitness_main, fitness_subs)

    order = np.argsort(fitness)
    league = league[order]
    fitness = fitness[order]

    league = np.reshape(league, (2*nteams, nmain, dim))

    league_main = league[0:2*nteams:2]
    league_subs = league[1:2*nteams:2]
    fitness_main = fitness[0:2*nteams:2]
    fitness_subs = fitness[1:2*nteams:2]
