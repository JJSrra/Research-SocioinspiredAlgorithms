import numpy as np

def UpdateFitnessAndHistory(CostFunction, population, population_fitness, history, history_fitness, emotion, emotion_decrease):
    former_best = np.min(history_fitness)

    # Compute new fitness for the new population
    population_fitness = np.apply_along_axis(CostFunction, 1, population)

    # Reorder population, history and emotions
    order = np.argsort(population_fitness)
    population_fitness = population_fitness[order]
    population = population[order]
    history = history[order]
    history_fitness[order]
    emotion = emotion[order]

    # Adapt emotion index depending on global performance
    emotion[np.where(population_fitness <= former_best)] -= emotion_decrease
    emotion[np.where(population_fitness > former_best)] = 1.0

    # Replace every individual history whose current fitness is the best
    history_changes = np.where(population_fitness < history_fitness)
    history[history_changes] = population[history_changes]
    history_fitness[history_changes] = population_fitness[history_changes]

    return population, population_fitness, history, history_fitness, emotion