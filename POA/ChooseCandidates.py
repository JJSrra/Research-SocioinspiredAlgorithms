import numpy as np

def ChooseCandidates(candidates, candidates_fitness, members, members_fitness):
    while (np.max(candidates_fitness) > np.min(members_fitness)):
        former_candidate_index = np.argmax(candidates_fitness)
        former_member_index = np.argmin(members_fitness)
        aux_position = np.copy(candidates[former_candidate_index])
        aux_fitness = np.copy(candidates_fitness[former_candidate_index])
        candidates[former_candidate_index] = members[former_member_index]
        candidates_fitness[former_candidate_index] = members_fitness[former_member_index]
        members[former_member_index] = aux_position
        members_fitness[former_member_index] = aux_fitness

    return candidates, candidates_fitness, members, members_fitness
