import numpy as np

def Manner1(individual, population, k1):
    return -k1 * np.random.uniform(0,1) * np.sum(population - individual, 0)

