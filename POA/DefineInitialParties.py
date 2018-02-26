import numpy as np

def DefineInitialParties(nparties, nmembers, ncandidates, dim, domain):
    lower_bound, upper_bound = domain
    total_members = nmembers + ncandidates

    # All the parliament is created as solutions, and splitted into parties
    parliament = np.random.uniform(lower_bound, upper_bound, nparties*total_members*dim).reshape(nparties, total_members, dim)
