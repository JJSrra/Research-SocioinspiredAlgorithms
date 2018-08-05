import numpy as np

def UpdateHistory(society, society_fitness, history, history_fitness):
    history_changes = np.where(society_fitness < history_fitness)
    history[history_changes] = society[history_changes]
    history_fitness[history_changes] = society_fitness[history_changes]

    return history, history_fitness