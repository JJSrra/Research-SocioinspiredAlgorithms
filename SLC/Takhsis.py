import numpy as np
from TestFoo import *

# Reorders the league and assigns best players to first team (main and subs) and so on.
def Takhsis(league_main, league_subs, fitness_main, fitness_subs, settings):

    nteams = settings['nteams']
    nmain = settings['nmain']
    nsubs = settings['nsubs']
    dim = settings['dim']

    # Both league arrays are merged into a common one, as well as both fitness arrays
    league = np.append(league_main, league_subs).reshape(nteams*(nmain+nsubs),dim)
    fitness = np.append(fitness_main, fitness_subs)

    # With the descending order of fitness given by argsort, both league and fitness arrays are reordered
    order = np.argsort(fitness)
    league = league[order]
    fitness = fitness[order]

    # An array of trues and falses is created for selecting which players are main and which subs players,
    # and to assign them to their matching team
    trues = [True for _ in range(nmain)]
    falses = [False for _ in range(nsubs)]
    per_team = np.append(trues, falses)
    per_league = np.array([per_team for _ in range(nteams)]).flatten()

    league_main = league[per_league].reshape(nteams,nmain,dim)
    league_subs = league[~per_league].reshape(nteams,nsubs,dim)

    # This works as well for selecting which fitness values correspond to main and subs teams
    fitness_main = fitness[per_league].reshape(nteams,nmain)
    fitness_subs = fitness[~per_league].reshape(nteams,nmain)

    return league_main, league_subs, fitness_main, fitness_subs
