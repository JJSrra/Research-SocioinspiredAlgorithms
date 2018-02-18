import numpy as np

def GenerateNewCountries(ncountries, dim, domain):
    lower_bound, upper_bound = domain

    # New countries are generated
    new_countries = np.random.uniform(lower_bound, upper_bound, ncountries*dim).reshape(ncountries,dim)

    return new_countries
