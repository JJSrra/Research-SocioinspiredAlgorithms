import numpy as np

def InternalIrregularity(current_fitness, history_best_fitness, internal_rate):
    return 1 - (np.e ** -internal_rate*(current_fitness - history_best_fitness))

def CalculateInternalIrregularityIndexes(society_fitness, history_fitness, internal_rate):
    return np.array([InternalIrregularity(current, past, internal_rate)
        for (current,past) in zip(society_fitness,history_fitness)])

def GeneratePreviousMovementPolicy(individual, internal_index, previous_best, internal_threshold, evolution_rate, domain):
    lower_bound, upper_bound = domain
    dim = len(individual)

    if internal_index < internal_threshold: 
        mutation_multiplier = np.random.uniform(-1,1,10)
        mutation = evolution_rate * mutation_multiplier * (previous_best - individual)
        return np.clip(individual + mutation, lower_bound, upper_bound)
    else:
        return np.random.uniform(lower_bound, upper_bound, dim)