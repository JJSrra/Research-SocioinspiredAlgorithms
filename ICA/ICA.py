# Imperialist Competitive Algorithm: A Socio Politically Inspired Optimization Strategy
# Developed By: Esmaeil Atashpaz Gargari
# Translated to Python By: Juanjo Sierra

from GenerateNewCountries import *
from CreateInitialEmpires import *
from AssimilateColonies import *
from RevolveColonies import *
from PosessEmpire import *

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
    initial_countries = GenerateNewCountries(ncountries, dim, domain)

    # New countries' cost/fitness is calculated
    fitness = np.apply_along_axis(CostFunction, 1, initial_countries)

    # And now the countries get sorted by their fitness
    order = np.argsort(fitness)
    fitness = fitness[order]
    initial_countries = initial_countries[order]

    # Initial empires are defined
    empires, empires_fitness, empires_total_cost = CreateInitialEmpires(initial_countries, fitness, nimperialists, zeta)

    # Main loop
    for decade in range(0,1):
        revolution_rate = damp_ratio*revolution_rate

        for i in range(0,len(empires)):
            # Assimilation: movement of colonies towards imperialists (Assimilation Policy)
            empires[i] = AssimilateColonies(empires[i], domain, assimilation_coef)

            # Revolution: a sudden change in the socio-political characteristics
            empires[i], empires_fitness[i], evals = RevolveColonies(empires[i],
                                empires_fitness[i], domain, revolution_rate, CostFunction)

            # Empire posession: if a colony has a lower cost than its imperialist, they switch positions
            empires[i], empires_fitness[i] = PosessEmpire(empires[i], empires_fitness[i])

            # Compute the current cost for each empire
            empires_total_cost[i] = empires_fitness[i][0] + zeta * np.mean(empires_fitness[i][1:])
