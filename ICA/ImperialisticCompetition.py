import numpy as np

def ImperialisticCompetition(imperialists, imperialists_fitness, colonies, colonies_fitness, empires_total_cost):
    dim = len(colonies[0][0])
    if np.random.rand() > 0.11:
        return imperialists, imperialists_fitness, colonies, colonies_fitness, empires_total_cost

    if len(imperialists) <= 1:
        return imperialists, imperialists_fitness, colonies, colonies_fitness, empires_total_cost

    # Search for the weakest empire (the one with the higher cost)
    weakest_empire = (-empires_total_cost).argsort()[0]
    max_total_cost = empires_total_cost[weakest_empire]
    total_powers = max_total_cost - empires_total_cost
    posession_probability = total_powers / np.sum(total_powers)

    # The empire that will conquer the colony is chosen
    selected_empire = SelectAnEmpire(posession_probability)
    selected_colony = np.random.randint(0, len(colonies[weakest_empire]))

    # Conquest
    colonies[selected_empire] = np.append(colonies[selected_empire], colonies[weakest_empire][selected_colony].reshape(1,dim), axis=0)
    colonies_fitness[selected_empire] = np.append(colonies_fitness[selected_empire], colonies_fitness[weakest_empire][selected_colony])

    # The colony is removed from its former empire
    colonies[weakest_empire] = np.delete(colonies[weakest_empire], selected_colony, 0)
    colonies_fitness[weakest_empire] = np.delete(colonies_fitness[weakest_empire], selected_colony)

    # If the weakest empire remains with one or less colonies (apart from the imperialist), it is also absorbed
    if len(colonies[weakest_empire]) <= 1:
        colonies_addition = np.append(colonies[weakest_empire], imperialists[weakest_empire].reshape(1,dim), axis=0)
        fitness_addition = np.append(colonies_fitness[weakest_empire], imperialists_fitness[weakest_empire])
        colonies[selected_empire] = np.append(colonies[selected_empire], colonies_addition, axis=0)
        colonies_fitness[selected_empire] = np.append(colonies_fitness[selected_empire], fitness_addition)

        del colonies[weakest_empire]
        del colonies_fitness[weakest_empire]
        imperialists = np.delete(imperialists, weakest_empire, 0)
        imperialists_fitness = np.delete(imperialists_fitness, weakest_empire)
        empires_total_cost = np.delete(empires_total_cost, weakest_empire)

    return imperialists, imperialists_fitness, colonies, colonies_fitness, empires_total_cost

# A function for selecting a random empire with given probabilities
def SelectAnEmpire(probability):
    r = np.random.rand(len(probability))
    d = probability - r

    # The empire with higher value will be selected
    selected = (-d).argsort()[0]
    return selected
