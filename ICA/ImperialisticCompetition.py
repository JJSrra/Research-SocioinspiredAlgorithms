import numpy as np

def ImperialisticCompetition(empires, empires_fitness, empires_total_cost):
    dim = len(empires[0][0])
    if np.random.rand() > 0.11:
        return empires, empires_fitness, empires_total_cost

    if len(empires) <= 1:
        return empires, empires_fitness, empires_total_cost

    # Search for the weakest empire (the one with the higher cost)
    weakest_empire = (-empires_total_cost).argsort()[0]
    max_total_cost = empires_total_cost[weakest_empire]
    total_powers = max_total_cost - empires_total_cost
    posession_probability = total_powers / np.sum(total_powers)

    # The empire that will conquer the colony is chosen
    selected_empire = SelectAnEmpire(posession_probability)
    selected_colony = np.random.randint(1, len(empires[weakest_empire]))

    # Conquest
    empires[selected_empire] = np.append(empires[selected_empire], empires[weakest_empire][selected_colony].reshape(1,dim), axis=0)
    empires_fitness[selected_empire] = np.append(empires_fitness[selected_empire], empires_fitness[weakest_empire][selected_colony])

    # The colony is removed from its former empire
    empires[weakest_empire] = np.delete(empires[weakest_empire], selected_colony, 0)
    empires_fitness[weakest_empire] = np.delete(empires_fitness[weakest_empire], selected_colony)

    # If the weakest empire remains with one or less colonies (apart from the imperialist), it is also absorbed
    if len(empires[weakest_empire]) <= 2:
        empires[selected_empire] = np.append(empires[selected_empire], empires[weakest_empire], axis=0)
        empires_fitness[selected_empire] = np.append(empires_fitness[selected_empire], empires_fitness[weakest_empire])

        del empires[weakest_empire]
        del empires_fitness[weakest_empire]
        empires_total_cost = np.delete(empires_total_cost, weakest_empire)

    return empires, empires_fitness, empires_total_cost

# A function for selecting a random empire with given probabilities
def SelectAnEmpire(probability):
    r = np.random.rand(len(probability))
    d = probability - r

    # The empire with higher value will be selected
    selected = (-d).argsort()[0]
    return selected
