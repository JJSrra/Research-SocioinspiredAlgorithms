import numpy as np

def Fickleness(current_fitness, iteration_best_fitness, best_past_fitness, fickleness_rate):
    return 1 - fickleness_rate*(iteration_best_fitness/current_fitness) - (1-fickleness_rate)*(best_past_fitness/current_fitness)

def CalculateFicklenessIndexes(society_fitness, history_fitness, fickleness_rate):
    best = np.min(society_fitness)
    
    return np.array([Fickleness(current, best, past, fickleness_rate)
        for (current, past) in zip(society_fitness, history_fitness)])

def GenerateCurrentMovementPolicy(individual, fickleness_index, iteration_best, fickleness_rate, evolution_rate, domain):
    lower_bound, upper_bound = domain
    dim = len(individual)

    if fickleness_index < fickleness_rate: 
        mutation_multiplier = np.random.uniform(-1,1,dim)
        mutation = evolution_rate * mutation_multiplier * (iteration_best - individual)
        return np.clip(individual + mutation, lower_bound, upper_bound)
    else:
        return np.random.uniform(lower_bound, upper_bound, dim)