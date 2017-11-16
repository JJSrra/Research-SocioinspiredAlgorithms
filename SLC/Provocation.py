import numpy as np
import random
from TestFoo import *

def Provocation(winner, league_main, league_subs, fitness_subs, settings):

    nsubs = settings['nsubs']
    lower_bound = settings['lower_bound']
    upper_bound = settings['upper_bound']
    dim = settings['dim']

    gravity = np.mean(league_main[winner], axis=0)
    chi_1 = random.uniform(0.9, 1)
    chi_2 = random.uniform(0.4, 0.6)

    new_player = np.clip(gravity + chi_1*(gravity - league_subs[winner][nsubs-1]), lower_bound, upper_bound)
    new_fitness = TestFoo(new_player)
    settings['neval'] += 1

    if new_fitness < fitness_subs[winner][nsubs-1]:
        league_subs[winner][nsubs-1] = new_player
        fitness_subs[winner][nsubs-1] = new_fitness
    else:
        new_player = np.clip(gravity + chi_2*(league_subs[winner][nsubs-1] - gravity), lower_bound, upper_bound)
        new_fitness = TestFoo(new_player)
        settings['neval'] += 1

        if new_fitness < fitness_subs[winner][nsubs-1]:
            league_subs[winner][nsubs-1] = new_player
            fitness_subs[winner][nsubs-1] = new_fitness
        else:
            league_subs[winner][nsubs-1] = np.random.uniform(lower_bound, upper_bound, dim)
            fitness_subs[winner][nsubs-1] = TestFoo(league_subs[winner][nsubs-1])
            settings['neval'] += 1

    return league_subs, fitness_subs, settings
