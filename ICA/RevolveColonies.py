import numpy as np
from GenerateNewCountries import *

def RevolveColonies(empire, empire_fitness, domain, revolution_rate, CostFunction):
    colonies = empire[1:len(empire)]
    colonies_fitness = empire_fitness[1:len(empire)]
    evals = 0

    # How many countries revolve depends on the revolution rate
    num_revolving_colonies = np.round(revolution_rate * len(colonies)).astype(int)
    dim = len(empire[0])

    # We only have to make new positions and recalculate if there is at least one colony to revolve
    if (num_revolving_colonies > 0):
        # Revolved colonies' positions are generated as new countries
        revolved_positions = GenerateNewCountries(num_revolving_colonies, dim, domain)

        randperm = np.random.permutation(len(colonies))
        colonies = colonies[randperm]
        colonies_fitness = colonies_fitness[randperm]

        # First 'num_revolving_colonies' are exchanged for their new positions
        colonies[0:num_revolving_colonies] = revolved_positions
        colonies_fitness[0:num_revolving_colonies] = np.apply_along_axis(CostFunction, 1, colonies[0:num_revolving_colonies])
        evals += num_revolving_colonies

        empire[1:len(empire)] = colonies
        empire_fitness[1:len(empire_fitness)] = colonies_fitness

    return empire, empire_fitness, evals
