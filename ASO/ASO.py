# Anarchic Society Optimization Algorithm
# As seen in the paper by Amir Ahmadi-Javid
# Implemented by Juanjo Sierra

from CreateInitialSociety import *
from CurrentMovementPolicy import CalculateFicklenessIndexes, GenerateCurrentMovementPolicy
from SocietyMovementPolicy import CalculateExternalIrregularityIndexes, GenerateSocietyMovementPolicy
from PreviousMovementPolicy import CalculateInternalIrregularityIndexes, GeneratePreviousMovementPolicy
from MovementPoliciesCombination import NewPositionsPolicyBased
from UpdateHistory import *

def ASO(CostFunction, dim=10, nindividuals=20, max_eval=10000,
    fickleness_rate=0.5, external_rate=4, external_threshold=0.5,
	internal_rate=4, internal_threshold=0.5, evolution_rate=0.5,
	lower_bound=0, upper_bound=10):

    # Domain of the function, tuple including lower and upper bounds
	domain = (lower_bound, upper_bound)

    # Create the initial society
	society, society_fitness, history, history_fitness = CreateInitialSociety(CostFunction,
            nindividuals, dim, domain)

	# Initial function evaluations are the same as society members
	evaluations = nindividuals

	# Start the main loop
	while evaluations < max_eval:
		global_best = np.min(history_fitness)
		iteration_best = society[np.argsort(society_fitness)[0]]

		fickleness_indexes = CalculateFicklenessIndexes(society_fitness, history_fitness, fickleness_rate)
		external_indexes = CalculateExternalIrregularityIndexes(society_fitness, global_best, external_rate)
		internal_indexes = CalculateInternalIrregularityIndexes(society_fitness, history_fitness, internal_rate)

		current_movement_positions = np.array([GenerateCurrentMovementPolicy(
			individual, fickleness_index, iteration_best, fickleness_rate, evolution_rate, domain)
			for (individual, fickleness_index) in zip(society, fickleness_indexes)])
		
		society_movement_positions = np.array([GenerateSocietyMovementPolicy(
			individual, external_index, global_best, external_threshold, evolution_rate, domain)
			for (individual, external_index) in zip(society, external_indexes)])

		previous_movement_positions = np.array([GeneratePreviousMovementPolicy(
			individual, internal_index, previous_best, internal_threshold, evolution_rate, domain)
			for (individual, internal_index, previous_best) in zip(society, internal_indexes, history)])

		society, society_fitness, new_evaluations = NewPositionsPolicyBased(CostFunction, current_movement_positions, society_movement_positions, previous_movement_positions)
		
		history, history_fitness = UpdateHistory(society, society_fitness, history, history_fitness)

		evaluations += new_evaluations
		
		#print("Iteration {:3}, best solution: {:e}".format(iteration, np.min(history_fitness)))

	return np.min(history_fitness)