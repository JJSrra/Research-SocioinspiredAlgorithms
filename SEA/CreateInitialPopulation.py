import numpy as np

def CreateInitialPopulation(CostFunction, nindividuals, dim, domain):
    lower_bound, upper_bound = domain

    # Create the N individuals with random positions in the search space
    population = np.random.uniform(lower_bound, upper_bound, nindividuals*dim).reshape(nindividuals, dim)
    population_fitness = np.apply_along_axis(CostFunction, 1, population)

    return population, population_fitness