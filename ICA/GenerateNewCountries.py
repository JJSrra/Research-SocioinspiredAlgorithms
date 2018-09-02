import numpy as np

def GenerateNewCountries(ncountries, dim, domain, initial_domain):
    lower_bound, upper_bound = domain
    initial_lower_bound, initial_upper_bound = initial_domain

    if initial_lower_bound != None and initial_upper_bound != None:
        lower_bound = initial_lower_bound
        upper_bound = initial_upper_bound

    # New countries are generated
    new_countries = np.random.uniform(lower_bound, upper_bound, ncountries*dim).reshape(ncountries,dim)

    return new_countries
