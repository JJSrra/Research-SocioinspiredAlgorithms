import numpy as np

def ExternalIrregularity(current_fitness, global_best_fitness, external_rate):
    return 1 - (np.e ** -external_rate*(current_fitness - global_best_fitness))

def CalculateExternalIrregularityIndexes(society_fitness, global_best_fitness, external_rate):
    return np.array([ExternalIrregularity(current, global_best_fitness, external_rate)
        for current in society_fitness])