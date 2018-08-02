import numpy as np

def Fickleness(current_fitness, iteration_best_fitness, best_past_fitness, fickleness_rate):
    return 1 - fickleness_rate*(iteration_best_fitness/current_fitness) - (1-fickleness_rate)*(best_past_fitness/current_fitness)

def CalculateFicklenessIndexes(society_fitness, history_fitness, fickleness_rate):
    best = np.min(society_fitness)
    
    return np.array([Fickleness(current, best, past, fickleness_rate)
        for (current, past) in zip(society_fitness, history_fitness)])