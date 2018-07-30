# Anarchic Society Optimization Algorithm
# As seen in the paper by Amir Ahmadi-Javid
# Implemented by Juanjo Sierra

from CreateInitialSociety import *

def ASO(CostFunction, dim=10, nindividuals=20, max_iter=1000,
    lower_bound=0, upper_bound=10):

    # Domain of the function, tuple including lower and upper bounds
	domain = (lower_bound, upper_bound)

    # Create the initial society
	society, society_fitness, history, history_fitness = CreateInitialSociety(CostFunction,
            nindividuals, dim, domain)
