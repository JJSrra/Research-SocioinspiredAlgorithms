import numpy as np

def PosessEmpire(imperialist, imperialist_fitness, colonies, colonies_fitness):
    best_colony = np.argmin(colonies_fitness)

    if (colonies_fitness[best_colony] < imperialist_fitness):
        old_imperialist = imperialist
        old_imperialist_fitness = imperialist_fitness
        imperialist = colonies[best_colony]
        imperialist_fitness = colonies_fitness[best_colony]
        colonies[best_colony] = old_imperialist
        colonies_fitness[best_colony] = old_imperialist_fitness

    return imperialist, imperialist_fitness, colonies, colonies_fitness
