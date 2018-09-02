import numpy as np
from ChooseCandidates import *

def DefineInitialParties(CostFunction, nparties, nmembers, ncandidates, dim, domain, initial_domain):
    lower_bound, upper_bound = domain
    initial_lower_bound, initial_upper_bound = initial_domain

    if initial_lower_bound != None and initial_upper_bound != None:
        lower_bound = initial_lower_bound
        upper_bound = initial_upper_bound

    nregularmembers = nmembers - ncandidates;

    # First we create the regular members of each party; it has to be saved in a list
    # because the size of the parties may vary in following steps of the algorithm
    members = np.random.uniform(lower_bound, upper_bound, nparties*nregularmembers*dim).reshape(nparties*nregularmembers, dim)
    members_fitness = np.apply_along_axis(CostFunction, 1, members)
    members = np.split(members, nparties)
    members_fitness = np.split(members_fitness, nparties)

    # And now we generate N candidate spots for each party, and assign each party's best members to them
    candidates = np.random.uniform(lower_bound, upper_bound, nparties*ncandidates*dim).reshape(nparties, ncandidates, dim)
    candidates_fitness = np.apply_along_axis(CostFunction, 2, candidates)

    for i in range(0,nparties):
        candidates[i], candidates_fitness[i], members[i], members_fitness[i] = ChooseCandidates(candidates[i],
                    candidates_fitness[i], members[i], members_fitness[i])

    return candidates, candidates_fitness, members, members_fitness
