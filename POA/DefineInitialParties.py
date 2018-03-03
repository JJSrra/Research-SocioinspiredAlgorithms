import numpy as np
from ChooseCandidates import *

def DefineInitialParties(CostFunction, nparties, nmembers, ncandidates, dim, domain):
    lower_bound, upper_bound = domain
    nregularmembers = nmembers - ncandidates;

    # First we create the regular members of each party; it has to be saved in a list
    # because the size of the parties may vary in following steps of the algorithm
    members = np.random.uniform(lower_bound, upper_bound, nparties*nregularmembers*dim).reshape(nparties, nregularmembers, dim)
    members_fitness = np.apply_along_axis(CostFunction, 2, members)

    # And now we generate N candidate spots for each party, and assign each party's best members to them
    candidates = np.random.uniform(lower_bound, upper_bound, nparties*ncandidates*dim).reshape(nparties, ncandidates, dim)
    candidates_fitness = np.apply_along_axis(CostFunction, 2, candidates)

    for i in range(0,nparties):
        candidates[i], candidates_fitness[i], members[i], members_fitness[i] = ChooseCandidates(candidates[i],
                    candidates_fitness[i], members[i], members_fitness[i])

    return candidates, candidates_fitness, members, members_fitness
