import numpy as np

def CreateInitialPopulation(CostFunction, nindividuals, dim, domain, initial_domain):
    lower_bound, upper_bound = domain
    initial_lower_bound, initial_upper_bound = initial_domain

    if initial_lower_bound != None and initial_upper_bound != None:
        lower_bound = initial_lower_bound
        upper_bound = initial_upper_bound

    # Create the N individuals with random positions in the search space
    population = np.random.uniform(lower_bound, upper_bound, nindividuals*dim).reshape(nindividuals, dim)
    population_fitness = np.apply_along_axis(CostFunction, 1, population)

    # Reorder the population, best individuals first
    # order = np.argsort(population_fitness)
    # population_fitness = population_fitness[order]
    # population = population[order]

    # We return a second population and fitness as the current history of best position for each individual
    return population, population_fitness, population, population_fitness