import numpy as np
import random
from TestFoo import *

def Imitation(winner, league_main, fitness_main, settings):

    nmain = settings['nmain']
    lower_bound = settings['lower_bound']
    upper_bound = settings['upper_bound']

    for i in range(0,nmain):
        tau = random.uniform(0.2, 0.8)
        player1 = random.randint(0, nmain-1)
        player2 = random.randint(0, nmain-1)

        new_player = np.clip(league_main[winner][i] + tau*(league_main[0][0] - league_main[winner][player1]), lower_bound, upper_bound)
        new_fitness = TestFoo(new_player)
        settings['neval'] += 1

        if new_fitness < fitness_main[winner][i]:
            league_main[winner][i] = new_player
            fitness_main[winner][i] = new_fitness
        else:
            new_player = np.clip(league_main[winner][i] +  tau*(league_main[winner][0] - league_main[winner][player1]), lower_bound, upper_bound)
            new_fitness = TestFoo(new_player)
            settings['neval'] += 1

            if new_fitness < fitness_main[winner][i]:
                league_main[winner][i] = new_player
                fitness_main[winner][i] = new_fitness
            else:
                new_player = np.clip(league_main[winner][i] +  tau*(league_main[winner][player2] - league_main[winner][player1]), lower_bound, upper_bound)
                new_fitness = TestFoo(new_player)
                settings['neval'] += 1

                if new_fitness < fitness_main[winner][i]:
                    league_main[winner][i] = new_player
                    fitness_main[winner][i] = new_fitness

    return league_main, fitness_main, settings
