import numpy as np

def CreateInitialEmpires(countries, fitness, nimperialists, zeta):

    num_colonies = np.shape(countries)[0] - nimperialists

    # Countries are divided into imperialists and colonies
    imperialists = countries[0:nimperialists]
    imperialists_fitness = fitness[0:nimperialists]
    colonies = countries[nimperialists:]
    colonies_fitness = fitness[nimperialists:]

    # Imperialist power is calculated
    if max(imperialists_fitness) > 0:
        imperialist_power = 1.3 * max(imperialists_fitness) - imperialists_fitness
    else:
        imperialist_power = 0.7 * max(imperialists_fitness) - imperialists_fitness

    # Number of colonies per imperialist are defined according to their power
    colonies_per_imperialist = np.round(imperialist_power/np.sum(imperialist_power) * num_colonies)

    # Given a random permutation of the colonies, they are splitted
    randperm = np.random.permutation(num_colonies)
    colonies = colonies[randperm]
    colonies_fitness = colonies_fitness[randperm]

    cumulative_colonies_per_imperialist = np.cumsum(colonies_per_imperialist).astype(int)
    new_colonies = np.split(colonies, cumulative_colonies_per_imperialist)[0:nimperialists]
    new_colonies_fitness = np.split(colonies_fitness, cumulative_colonies_per_imperialist)
    empires_total_cost = np.array([])

    for i in range(0,nimperialists):
        empires_total_cost = np.append(empires_total_cost, imperialists_fitness[i] + zeta * np.mean(colonies_fitness[i]))

    return imperialists, imperialists_fitness, new_colonies, new_colonies_fitness, empires_total_cost
