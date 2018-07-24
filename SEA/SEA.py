# Social Emotional Optimization Algorithm for Nonlinear Constrained Optimization Problems
# As seen in the paper by Yuechun Xu, Zhihua Cui & Jianchao Zeng
# Implemented by Juanjo Sierra

from CreateInitialPopulation import *
from Manners import Manner1
from UpdateFitnessAndHistory import *
from BehaviourChanges import *

def SEA(CostFunction, dim=10, nindividuals=20, max_iter=500,
	k1=0.01, k2=0.02, k3=0.03, emotion_decrease=0.05, lower_threshold=0.3,
	upper_threshold=0.6, lower_bound=0, upper_bound=10):

	# Domain of the function, tuple including lower and upper bounds
	domain = (lower_bound, upper_bound)

	# Create the first individuals
	population, population_fitness, history, history_fitness = CreateInitialPopulation(CostFunction,
			nindividuals, dim, domain)

	# Create emotion indexes
	emotion = np.ones(nindividuals)

	# First behaviour change
	manner = np.array([Manner1(individual, population, k1) for individual in population])
	population = np.clip(population + manner, lower_bound, upper_bound)

	# Update new positions, fitness and history
	population_fitness, history, history_fitness, emotion = UpdateFitnessAndHistory(CostFunction,
			population, population_fitness, history, history_fitness, emotion, emotion_decrease)

	# Update best global solution
	status_best = history[np.argsort(history_fitness)[0]]

	# Start iterations
	for iteration in range(0, max_iter):

		# Change behaviours according to emotion indexes
		population = BehaviourChanges(population, population_fitness, history, status_best, emotion,
				lower_threshold, upper_threshold, k1, k2, k3, domain)

		# Update new positions, fitness and history
		population_fitness, history, history_fitness, emotion = UpdateFitnessAndHistory(CostFunction,
			population, population_fitness, history, history_fitness, emotion, emotion_decrease)

		# Update best global solution
		status_best = history[np.argsort(history_fitness)[0]]

		print("Iteration {:3}, best solution: {:e}".format(iteration, np.min(history_fitness)))

