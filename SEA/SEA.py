# Social Emotional Optimization Algorithm for Nonlinear Constrained Optimization Problems
# As seen in the paper by Yuechun Xu, Zhihua Cui & Jianchao Zeng
# Implemented by Juanjo Sierra

from CreateInitialPopulation import *
from Manners import Manner1
from UpdateFitnessAndHistory import *
from BehaviourChanges import *

def SEA(CostFunction, dim=10, nindividuals=20, max_eval=10000,
	k1=0.01, k2=0.02, k3=0.03, emotion_decrease=0.05, lower_threshold=0.3,
	upper_threshold=0.6, lower_bound=0, upper_bound=10):

	# Domain of the function, tuple including lower and upper bounds
	domain = (lower_bound, upper_bound)

	# Create the first individuals
	population, population_fitness, history, history_fitness = CreateInitialPopulation(CostFunction,
			nindividuals, dim, domain)

	# Initial evaluations (history evaluations don't count)
	evaluations = nindividuals

	# Create emotion indexes
	emotion = np.ones(nindividuals)

	# First behaviour change
	manner = np.array([Manner1(individual, population, k1) for individual in population])
	population = np.clip(population + manner, lower_bound, upper_bound)

	# Update new positions, fitness and history
	population_fitness, history, history_fitness, emotion, new_evaluations = UpdateFitnessAndHistory(CostFunction,
			population, population_fitness, history, history_fitness, emotion, emotion_decrease)

	evaluations += new_evaluations

	# Update best global solution
	status_best = history[np.argsort(history_fitness)[0]]

	evaluations_marker = 0
	evaluation_marks = np.array([])

	# Start iterations
	while evaluations < max_eval:
		# Change behaviours according to emotion indexes
		population = BehaviourChanges(population, population_fitness, history, status_best, emotion,
				lower_threshold, upper_threshold, k1, k2, k3, domain)

		# Update new positions, fitness and history
		population_fitness, history, history_fitness, emotion, new_evaluations = UpdateFitnessAndHistory(CostFunction,
			population, population_fitness, history, history_fitness, emotion, emotion_decrease)

		evaluations += new_evaluations

		# Update best global solution
		status_best = history[np.argsort(history_fitness)[0]]

		if evaluations >= evaluations_marker:
			evaluation_marks = np.insert(evaluation_marks, len(evaluation_marks), np.min(history_fitness))
			evaluations_marker += max_eval / 10

		# print("Iteration {:3}, best solution: {:e}".format(iteration, np.min(history_fitness)))

	return np.append(evaluation_marks, np.min(history_fitness))

