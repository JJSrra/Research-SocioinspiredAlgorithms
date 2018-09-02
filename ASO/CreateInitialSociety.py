import numpy as np

def CreateInitialSociety(CostFunction, nindividuals, dim, domain, initial_domain):
    lower_bound, upper_bound = domain
    initial_lower_bound, initial_upper_bound = initial_domain

    if initial_lower_bound != None and initial_upper_bound != None:
        lower_bound = initial_lower_bound
        upper_bound = initial_upper_bound

    # Create first nindividuals
    society = np.random.uniform(lower_bound, upper_bound, nindividuals*dim).reshape(nindividuals, dim)
    society_fitness = np.apply_along_axis(CostFunction, 1, society)

    # Society structures are duplicated for storing best past position per member
    return society, society_fitness, society, society_fitness