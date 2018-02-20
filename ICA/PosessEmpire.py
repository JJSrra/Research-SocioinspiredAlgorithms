import numpy as np

def PosessEmpire(empire, empire_fitness):
    colonies_fitness = empire_fitness[1:len(empire_fitness)]
    best_colony = np.argmin(colonies_fitness)

    if (empire_fitness[best_colony+1] < empire_fitness[0]):
        old_imperialist = empire[0]
        old_imperialist_fitness = empire_fitness[0]
        empire[0] = empire[best_colony+1]
        empire_fitness[0] = empire_fitness[best_colony+1]
        empire[best_colony+1] = old_imperialist
        empire_fitness[best_colony+1] = old_imperialist_fitness

    return empire, empire_fitness
