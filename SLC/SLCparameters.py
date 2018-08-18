import optproblems.cec2005
import numpy as np
import time
from SLC import *

if __name__ == "__main__":
    dim = 10
    repeats = 10
    evaluations = 10000*dim
    teams = 5
    main_players = 3
    sub_players = 3
    mutation_probabilities = [0.05,0.1,0.2]
    mutation_rates = [0.1,0.2,0.3]

    f1 = optproblems.cec2005.F1(dim)
    print("F1: Shifted Sphere Function\n")

    for mprobability in mutation_probabilities:
        for mrate in mutation_rates:
            time1 = time.time()
            results = np.array([SLC(f1, dim=dim, max_eval=evaluations, nteams=teams,
                nmain=main_players, nsubs=sub_players, mutation_probability=mprobability,
                mutation_rate=mrate, lower_bound=-100, upper_bound=100) for _ in range(repeats)])
            total_time = time.time() - time1
            print("Mutation probability: {}\tMutation rate: {}".format(mprobability, mrate))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")

    print("###############################################")

    f6 = optproblems.cec2005.F6(dim)
    print("F6: Shifted Rosenbrock’s Function\n")

    for mprobability in mutation_probabilities:
        for mrate in mutation_rates:
            time1 = time.time()
            results = np.array([SLC(f6, dim=dim, max_eval=evaluations, nteams=teams,
                nmain=main_players, nsubs=sub_players, mutation_probability=mprobability,
                mutation_rate=mrate, lower_bound=-100, upper_bound=100) for _ in range(repeats)])
            total_time = time.time() - time1
            print("Mutation probability: {}\tMutation rate: {}".format(mprobability, mrate))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")

    print("###############################################")

    f14 = optproblems.cec2005.F14(dim)
    print("F14: Shifted Rotated Expanded Scaffer’s F6\n")

    for mprobability in mutation_probabilities:
        for mrate in mutation_rates:
            time1 = time.time()
            results = np.array([SLC(f14, dim=dim, max_eval=evaluations, nteams=teams,
                nmain=main_players, nsubs=sub_players, mutation_probability=mprobability,
                mutation_rate=mrate, lower_bound=-100, upper_bound=100) for _ in range(repeats)])
            total_time = time.time() - time1
            print("Mutation probability: {}\tMutation rate: {}".format(mprobability, mrate))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")

    print("###############################################")

    f15 = optproblems.cec2005.F15(dim)
    print("F15: Hybrid Composition Function\n")

    for mprobability in mutation_probabilities:
        for mrate in mutation_rates:
            time1 = time.time()
            results = np.array([SLC(f15, dim=dim, max_eval=evaluations, nteams=teams,
                nmain=main_players, nsubs=sub_players, mutation_probability=mprobability,
                mutation_rate=mrate, lower_bound=-5, upper_bound=5) for _ in range(repeats)])
            total_time = time.time() - time1
            print("Mutation probability: {}\tMutation rate: {}".format(mprobability, mrate))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")