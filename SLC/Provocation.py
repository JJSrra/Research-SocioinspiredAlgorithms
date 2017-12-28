import numpy as np
import random

def Provocation(CostFunction, winner, league_main, league_subs, fitness_subs, domain, evals_competition):

    nsubs = league_subs.shape[1]
    dim = league_subs.shape[2]
    lower_bound, upper_bound = domain

    gravity = np.mean(league_main[winner], axis=0)
    chi_1 = random.uniform(0.9, 1)
    chi_2 = random.uniform(0.4, 0.6)

    new_player = np.clip(gravity + chi_1*(gravity - league_subs[winner][nsubs-1]), lower_bound, upper_bound)
    new_fitness = CostFunction(new_player)
    evals_competition += 1

    if new_fitness < fitness_subs[winner][nsubs-1]:
        league_subs[winner][nsubs-1] = new_player
        fitness_subs[winner][nsubs-1] = new_fitness
    else:
        new_player = np.clip(gravity + chi_2*(league_subs[winner][nsubs-1] - gravity), lower_bound, upper_bound)
        new_fitness = CostFunction(new_player)
        evals_competition += 1

        if new_fitness < fitness_subs[winner][nsubs-1]:
            league_subs[winner][nsubs-1] = new_player
            fitness_subs[winner][nsubs-1] = new_fitness
        else:
            league_subs[winner][nsubs-1] = np.random.uniform(lower_bound, upper_bound, dim)
            fitness_subs[winner][nsubs-1] = CostFunction(league_subs[winner][nsubs-1])
            evals_competition += 1

    return league_subs, fitness_subs, evals_competition
