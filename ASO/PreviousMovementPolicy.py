import numpy as np

def InternalIrregularity(current_fitness, history_best_fitness, internal_rate):
    return 1 - (np.e ** -internal_rate*(current_fitness - history_best_fitness))

def CalculateInternalIrregularityIndexes(society_fitness, history_fitness, internal_rate):
    return np.array([InternalIrregularity(current, past, internal_rate)
        for (current,past) in zip(society_fitness,history_fitness)])