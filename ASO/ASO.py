# Anarchic Society Optimization Algorithm
# As seen in the paper by Amir Ahmadi-Javid
# Implemented by Juanjo Sierra

from CreateInitialSociety import *
from CurrentMovementPolicy import CalculateFicklenessIndexes

def ASO(CostFunction, dim=10, nindividuals=20, max_iter=1000,
    fickleness_rate=0.3, external_threshold=0.5, internal_threshold=0.5,
	lower_bound=0, upper_bound=10):

    # Domain of the function, tuple including lower and upper bounds
	domain = (lower_bound, upper_bound)

    # Create the initial society
	society, society_fitness, history, history_fitness = CreateInitialSociety(CostFunction,
            nindividuals, dim, domain)

	# Start the main loop
	iteration = 0
	while iteration < max_iter:
		fickleness_indexes = CalculateFicklenessIndexes(society_fitness, history_fitness, fickleness_rate)
		
		iteration += 1