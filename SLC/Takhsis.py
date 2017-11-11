import numpy as np
from TestFoo import *

def Takhsis(league_main, league_subs, fitness_main, fitness_subs, settings):

    nteams = settings['nteams']
    nmain = settings['nmain']
    nsubs = settings['nsubs']
    dim = settings['dim']

    league = np.append(league_main, league_subs).reshape(nteams*(nmain+nsubs),dim)
    fitness = np.append(fitness_main, fitness_subs)

    order = np.argsort(fitness)
    league = league[order]
    fitness = fitness[order]

    trues = [True for _ in range(nmain)]
    falses = [False for _ in range(nsubs)]
    per_team = np.append(trues, falses)
    per_league = np.array([per_team for _ in range(nteams)]).flatten()

    league_main = league[per_league].reshape(nteams,nmain,dim)
    league_subs = league[~per_league].reshape(nteams,nsubs,dim)

    fitness_main = fitness[per_league]
    fitness_subs = fitness[~per_league]

    return league_main, league_subs, fitness_main, fitness_subs
