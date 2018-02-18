# Imperialist Competitive Algorithm: A Socio Politically Inspired Optimization Strategy
# Developed By: Esmaeil Atashpaz Gargari
# Translated to Python By: Juanjo Sierra

from GenerateNewCountries import *
from CreateInitialEmpires import *

def ICA(CostFunction, dim=30, ncountries=200, nimperialists=8, decades=2000,
        revolution_rate=0.3, assimilation_coef=2, assimilation_angle_coef=0.5,
        zeta=0.02, damp_ratio=0.99, stop_if_just_one_empire=False, uniting_threshold=0.02,
        lower_bound=0, upper_bound=10):

    # Zarib is used to prevent the weakest empire to have a probability of zero
    zarib = 1.05
    # Alpha is the importance of the mean minimun compared to the global minimum. Must be << 1
    alpha = 0.1
    # Domain of the problem, tuple including lower and upper bounds
    domain = (lower_bound, upper_bound)

    # Generation of the initial countries
    initial_countries, fitness = GenerateNewCountries(ncountries, dim, domain, CostFunction)

    # Initial empires are defined
    empires, empires_fitness, empires_total_cost = CreateInitialEmpires(initial_countries, fitness, nimperialists, zeta)
