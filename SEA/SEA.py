# Social Emotional Optimization Algorithm for Nonlinear Constrained Optimization Problems
# As seen in the paper by Yuechun Xu, Zhihua Cui & Jianchao Zeng
# Implemented by Juanjo Sierra

from CreateInitialPopulation import *

def SEA(CostFunction, dim=10, nindividuals=20, max_iter=500,
    lower_bound=0, upper_bound=10):

    # Domain of the function, tuple including lower and upper bounds
    domain = (lower_bound, upper_bound)

    # Create the first individuals
    population, population_fitness = CreateInitialPopulation(CostFunction, nindividuals, dim, domain)