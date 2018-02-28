# Parliamentary Political Competitions: A New Approach To Global Optimization
# As seen in the paper by Ali Borji & Mandana Hamidi
# Implemented by Juanjo Sierra

from DefineInitialParties import *

def POA(CostFunction, dim=30, nparties=10, nregularmembers=45, ncandidates=5,
        lower_bound=0, upper_bound=10): # Any settings will be arguments of this function

    # Domain of the function, tuple including lower and upper bounds
    domain = (lower_bound, upper_bound)

    # Define the initial parties and candidates
    candidates, candidates_fitness, members, members_fitness = DefineInitialParties(CostFunction,
                nparties, nregularmembers, ncandidates, dim, domain)
