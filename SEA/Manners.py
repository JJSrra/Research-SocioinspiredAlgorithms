import numpy as np

def Manner1(population, k1):
    nindividuals = len(population)
    dim = len(population[0])

    manner = np.zeros(nindividuals * dim).reshape(nindividuals, dim)

    for i in range(0,nindividuals):
        manner[i] = -k1 * np.random.uniform(0,1) * np.sum(population - population[i], 0)

    return manner