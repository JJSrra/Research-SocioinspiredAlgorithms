import numpy as np
from ChooseCandidates import *

def InterGroupCooperation(candidates, candidates_fitness, members, members_fitness,
        group_power, groups_to_merge, merge_probability, groups_to_delete, deletion_probability):

    # First a random number is generated to check if the most powerful groups merge
    if len(candidates) >= groups_to_merge:
        random_number = np.random.rand()

        if random_number < merge_probability:
            for _ in range(1,groups_to_merge):
                best, second = np.argsort(group_power)[0:2]

                # Make the members that will be merged join the best party
                members_addition = np.append(members[second], candidates[second], axis=0)
                fitness_addition = np.append(members_fitness[second], candidates_fitness[second])
                members[best] = np.append(members[best], members_addition, axis=0)
                members_fitness[best] = np.append(members_fitness[best], fitness_addition)

                # Delete the appended group
                del members[second]
                del members_fitness[second]
                candidates = np.delete(candidates, second, 0)
                candidates_fitness = np.delete(candidates_fitness, second, 0)
                group_power = np.delete(group_power, second)

            # After the merging, candidates are reassigned
            best = np.argsort(group_power)[0]
            candidates[best], candidates_fitness[best], members[best], members_fitness[best] = ChooseCandidates(candidates[best],
                    candidates_fitness[best], members[best], members_fitness[best])


    # Next step is checking if is it possible to delete the weakest groups
    if len(candidates) > groups_to_delete:
        random_number = np.random.rand()

        if random_number < deletion_probability:
            for _ in range(0,groups_to_delete):
                worst = np.argsort(group_power)[-1]

                # Delete the worst group
                del members[worst]
                del members_fitness[worst]
                candidates = np.delete(candidates, worst, 0)
                candidates_fitness = np.delete(candidates_fitness, worst, 0)
                group_power = np.delete(group_power, worst)


    return candidates, candidates_fitness, members, members_fitness, group_power
