import numpy as np
import math

def LoserFunction(CostFunction, loser, league_main, fitness_main, league_subs, fitness_subs, mutation_rate, mutation_probability, domain, evals_competition):

    nmain,dim = league_main.shape[1:]
    nsubs = league_subs.shape[1]

    # Player that are being mutated are selected from a permutation of the loser team
    main_selected = np.random.permutation(np.arange(nmain))[0:3]

    # Number of mutations that will affect the selected players (at least 1, due to the ceil function)
    num_mutations = math.ceil(mutation_probability*dim)

    for i in range(3):
        # Components mutated are different for each player
        components_mutated = np.random.permutation(np.arange(dim))[0:num_mutations]

        # Array with the mutations that will be applied to each component
        mutations = np.random.uniform(-1,1,num_mutations)

        # If the array is not copied intentionally, it will not be possible to check
        # the 'former' player after being mutated
        mutated_player = np.array(league_main[loser][main_selected[i]])
        mutated_player[components_mutated] += mutation_rate * mutations

        # Fitness evaluation of the mutated players
        mutated_fitness = CostFunction(mutated_player)
        evals_competition += 1

        # If any mutated player is better than its former self, it is now replaced
        if mutated_fitness < fitness_main[loser][main_selected[i]]:
            league_main[loser][main_selected[i]] = mutated_player
            fitness_main[loser][main_selected[i]] = mutated_fitness


    # Crossover between subs players of the loser team
    new_mutations = [None for _ in range(2*nsubs)]
    new_fitness = [None for _ in range(2*nsubs)]

    for i in range(nsubs):
        # 2 random subs players are main_selected
        subs_selected = np.random.permutation(np.arange(nsubs))[0:2]

        # Alpha array that will affect the combination of the solutions
        alpha = np.random.uniform(0,1,dim)

        # 2 new players are generated combining both selected players with alpha weights
        new_mutations[i*2] = alpha*league_subs[loser][subs_selected[0]] + (1-alpha)*league_subs[loser][subs_selected[1]]
        new_mutations[(i*2)+1] = alpha*league_subs[loser][subs_selected[1]] + (1-alpha)*league_subs[loser][subs_selected[0]]

        new_fitness[i*2] = CostFunction(new_mutations[i*2])
        new_fitness[(i*2)+1] = CostFunction(new_mutations[(i*2)+1])
        evals_competition += 2

    # All players are gathered, and then they will be reordered and worst players are left out
    all_players = np.concatenate((league_main[loser], league_subs[loser], new_mutations))
    all_fitness = np.concatenate((fitness_main[loser], fitness_subs[loser], new_fitness))

    # Players are reordered and reassigned the same as in Takhsis function
    order = np.argsort(all_fitness)
    all_players = all_players[order]
    all_fitness = all_fitness[order]

    league_main[loser] = all_players[0:nmain]
    fitness_main[loser] = all_fitness[0:nmain]
    league_subs[loser] = all_players[nmain:(nmain+nsubs)]
    fitness_subs[loser] = all_fitness[nmain:(nmain+nsubs)]

    return league_main, fitness_main, league_subs, fitness_subs, evals_competition
