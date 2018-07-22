import numpy as np
from Manners import Manner2

def BehaviourChanges(population, population_fitness, history, history_fitness, emotion, lower_threshold, upper_threshold, k1, k2, k3, domain):
    lower_bound, upper_bound = domain
    status_best = history[np.argsort(history_fitness)[0]]

    # Select as 'bad population' individuals with emotion index lesser than lower threshold
    bad_population = np.where(emotion < lower_threshold)

    if (len(bad_population[0] > 0)):
        population[bad_population] += np.array([Manner2(individual, status_best, k2) 
                for individual in population[bad_population]])
    
