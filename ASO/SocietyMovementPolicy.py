import numpy as np

def ExternalIrregularity(current_fitness, global_best_fitness, external_rate):
    return 1 - (np.e ** -external_rate*(current_fitness - global_best_fitness))

def CalculateExternalIrregularityIndexes(society_fitness, global_best_fitness, external_rate):
    return np.array([ExternalIrregularity(current, global_best_fitness, external_rate)
        for current in society_fitness])

def GenerateSocietyMovementPolicy(individual, external_index, global_best, external_threshold, evolution_rate, domain):
    lower_bound, upper_bound = domain
    dim = len(individual)

    if external_index < external_threshold: 
        mutation_multiplier = np.random.uniform(-1,1,dim)
        mutation = evolution_rate * mutation_multiplier * (global_best - individual)
        return np.clip(individual + mutation, lower_bound, upper_bound)
    else:
        return np.random.uniform(lower_bound, upper_bound, dim)