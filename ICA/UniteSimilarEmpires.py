import numpy as np

def UniteSimilarEmpires(imperialists, imperialists_fitness, colonies, colonies_fitness, empires_total_cost, domain, uniting_threshold, zeta):
    lower_bound, upper_bound = domain
    dim = len(colonies[0][0])

    # The threshold distance is the lower distance two imperialists can be separated by without merging
    threshold_distance = uniting_threshold * abs(upper_bound - lower_bound)

    # Check if there is a pair of empires that much closer
    for i in range(0, len(imperialists)):
        for j in range(i+1, len(imperialists)):
            distance_vector = imperialists[i] - imperialists[j]
            distance = np.linalg.norm(distance_vector)

            # If there is such a pair, the empire with the
            # best (lower-cost) imperialist absorbs the other empire
            if distance <= threshold_distance:
                if imperialists_fitness[i] < imperialists_fitness[j]:
                    best_imperialist = i
                    worst_imperialist = j
                else:
                    best_imperialist = j
                    worst_imperialist = i

                colonies_addition = np.append(colonies[worst_imperialist], imperialists[worst_imperialist].reshape(1,dim), axis=0)
                fitness_addition = np.append(colonies_fitness[worst_imperialist], imperialists_fitness[worst_imperialist])
                colonies[best_imperialist] = np.append(colonies[best_imperialist], colonies_addition, axis=0)
                colonies_fitness[best_imperialist] = np.append(colonies_fitness[best_imperialist], fitness_addition)
                empires_total_cost[best_imperialist] = imperialists_fitness[best_imperialist] + zeta * np.mean(colonies_fitness[best_imperialist])

                # And we get rid of the absorbed empire position
                del colonies[worst_imperialist]
                del colonies_fitness[worst_imperialist]
                imperialists = np.delete(imperialists, worst_imperialist, 0)
                imperialists_fitness = np.delete(imperialists_fitness, worst_imperialist)
                empires_total_cost = np.delete(empires_total_cost, worst_imperialist)
                return imperialists, imperialists_fitness, colonies, colonies_fitness, empires_total_cost

    return imperialists, imperialists_fitness, colonies, colonies_fitness, empires_total_cost
