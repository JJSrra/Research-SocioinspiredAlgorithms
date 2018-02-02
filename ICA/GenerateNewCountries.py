import numpy as np

def GenerateNewCountries(ncountries, dim, domain, CostFunction):
    lower_bound, upper_bound = domain

    # New countries are generated
    new_countries = np.random.uniform(lower_bound, upper_bound, ncountries*dim).reshape(ncountries,dim)

    # New countries' cost/fitness is calculated
    new_fitness = np.apply_along_axis(CostFunction, 1, new_countries)

    # And now the countries get sorted by their fitness
    order = np.argsort(new_fitness)
    new_fitness = new_fitness[order]
    new_countries = new_countries[order]

    return new_countries, new_fitness
