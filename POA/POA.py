# Parliamentary Political Competitions: A New Approach To Global Optimization
# As seen in the paper by Ali Borji & Mandana Hamidi
# Implemented by Juanjo Sierra

from DefineInitialParties import *
from IntraGroupCompetition import *

def POA(CostFunction, dim=30, nparties=4, nmembers=5, ncandidates=2,
        lower_bound=0, upper_bound=10, max_iter=30000, merge_probability=0.01,
        deletion_probability=0.001, bias=0.3, member_weighting=0.01,
        candidate_weighting=1, gropus_to_merge=2, gropus_to_delete=1):

    # Domain of the function, tuple including lower and upper bounds
    domain = (lower_bound, upper_bound)

    # Define the initial parties and candidates
    candidates, candidates_fitness, members, members_fitness = DefineInitialParties(CostFunction,
                    nparties, nmembers, ncandidates, dim, domain)

    iterations = 29999
    group_power = np.zeros(nparties)

    while iterations < max_iter:
        for i in range(0,len(candidates)):
            candidates[i], candidates_fitness[i], members[i], members_fitness[i], group_power[i] = IntraGroupCompetition(CostFunction,
                    candidates[i], candidates_fitness[i], members[i], members_fitness[i], domain,
                    bias, candidate_weighting, member_weighting)

        iterations += 1
