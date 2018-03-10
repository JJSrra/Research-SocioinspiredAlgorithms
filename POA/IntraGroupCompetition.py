import numpy as np
import numpy.matlib
from ChooseCandidates import *

def IntraGroupCompetition(CostFunction, candidates, candidates_fitness, members, members_fitness, domain, bias, candidate_weighting, member_weighting):
    lower_bound, upper_bound = domain
    dim = len(candidates[0])

    # Regular members of a party are biased toward candidates
    candidates_rep = np.matlib.repmat(candidates, len(members), 1).reshape(len(members),len(candidates),dim)
    members_rep = np.repeat(members, len(candidates), axis=0).reshape(len(members),len(candidates),dim)
    fitness_rep = np.matlib.repmat(candidates_fitness, len(members), 1).reshape(len(members),len(candidates),1)
    dif = candidates_rep - members_rep

    # Operations as in the formula seen in the paper
    sum_up = np.apply_along_axis(sum, 1, dif*fitness_rep)
    sum_down = np.sum(candidates_fitness)
    possible_changes = members + bias*(sum_up/sum_down)

    # Now we have to check which members are going to change, only if they have upgraded their fitness
    new_fitness = np.apply_along_axis(CostFunction, 1, possible_changes)
    change_index = np.where(new_fitness < members_fitness)
    members[change_index] = possible_changes[change_index]
    members_fitness[change_index] = new_fitness[change_index]

    # And then check if any new regular member deserves to be a candidate
    candidates, candidates_fitness, members, members_fitness = ChooseCandidates(candidates, candidates_fitness, members, members_fitness)

    # Finally, we compute the power of the group according to the formula in the paper
    power = (candidate_weighting*np.mean(candidates_fitness) + member_weighting*np.mean(members_fitness)) / candidate_weighting+member_weighting

    return candidates, candidates_fitness, members, members_fitness, power
