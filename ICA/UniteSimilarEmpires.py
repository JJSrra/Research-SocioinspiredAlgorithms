import numpy as np

def UniteSimilarEmpires(empires, empires_fitness, domain, uniting_threshold):
    lower_bound, upper_bound = domain

    # The threshold distance is the lower distance two imperialists can be separated by without merging
    threshold_distance = uniting_threshold * abs(upper_bound - lower_bound)

    # Check if there is a pair of empires that much closer
    for i in range(0, len(empires)):
        for j in range(i+1, len(empires)):
            distance_vector = empires[i][0] - empires[j][0]
            distance = np.linalg.norm(distance_vector)

            # If there is such a pair, the empire with the
            # best (lower-cost) imperialist absorbs the other empire
            if distance <= threshold_distance:
                if empires_fitness[i][0] < empires_fitness[j][0]:
                    best_imperialist = i
                    worst_imperialist = j
                else:
                    best_imperialist = j
                    worst_imperialist = i

                print("\nMejor: {}".format(len(empires[best_imperialist])))
                print("Peor: {}".format(len(empires[worst_imperialist])))

                empires[best_imperialist] = np.append(empires[best_imperialist], empires[worst_imperialist], axis=0)
                empires_fitness[best_imperialist] = np.append(empires_fitness[best_imperialist], empires_fitness[worst_imperialist])

                print("Nuevo mejor: {}".format(len(empires[best_imperialist])))
                print("Peor: {}".format(len(empires[worst_imperialist])))

                # And we get rid of the absorbed empire position
                del empires[worst_imperialist]
                del empires_fitness[worst_imperialist]
                break

    return empires, empires_fitness
