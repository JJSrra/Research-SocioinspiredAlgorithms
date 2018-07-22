import numpy as np
from Manners import Manner2, Manner3

def BehaviourChanges(population, population_fitness, history, history_fitness, emotion, lower_threshold, upper_threshold, k1, k2, k3, domain):
    lower_bound, upper_bound = domain
    status_best = history[np.argsort(history_fitness)[0]]

    emotion = np.random.uniform(0.2, 0.8, 20)

    # Select as 'bad population' individuals with emotion index lesser than lower threshold
    bad_population = np.where(emotion < lower_threshold)

    # Select as 'average population' individuals with emotion index between lower and upper thresholds
    average_population = np.where(np.logical_and(emotion >= lower_threshold, emotion < upper_threshold))

    # Perform appropriate change to bad population
    if(len(bad_population[0] > 0)):
        population[bad_population] += np.array([Manner2(individual, status_best, k2) 
                for individual in population[bad_population]])

    # Perform appropriate change to average population
    if(len(average_population[0] > 0)):
        population[average_population] += np.array([Manner3(individual, individual_best, status_best, population, k1, k2, k3) 
                for (individual, individual_best) in zip(population[average_population], history[average_population])])
    