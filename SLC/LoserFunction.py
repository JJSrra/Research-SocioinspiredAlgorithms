import numpy as np
import math

def LoserFunction(CostFunction, loser, league_main, fitness_main, league_subs, fitness_subs, mutation_rate, mutation_probability, domain, evals_competition):

    nmain,dim = league_main.shape[1:]

    # Player that are being mutated are selected from a permutation of the loser team
    main_selected = np.random.permutation(np.arange(nmain))[0:3]

    # Number of mutations that will affect the selected players (at least 1, due to the ceil function)
    num_mutations = math.ceil(mutation_probability*dim)

    for i in range(3):
        # Components mutated are different for each player
        components_mutated = np.random.permutation(np.arange(dim))[0:num_mutations]

        # If the array is not copied intentionally, it will not be possible to check
        # the 'former' player after being mutated
        mutated_player = np.array(league_main[loser][main_selected[i]])
        mutated_player[components_mutated] += mutation_rate * num_mutations

        mutated_fitness = CostFunction(mutated_player)
        evals_competition += 1

        if mutated_fitness < fitness_main[loser][main_selected[i]]:
            league_main[loser][main_selected[i]] = mutated_player
            fitness_main[loser][main_selected[i]] = mutated_fitness

    return league_main, fitness_main, league_subs, fitness_subs, evals_competition
