import cec2014
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

    np.random.seed(10)

    def f1(x):
        return cec2014.cec14(x,1)
    
    print("F1: Rotated High Conditioned Elliptic Function\n")

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

    np.random.seed(10)

    def f4(x):
        return cec2014.cec14(x,4)
    
    print("F4: Shifted and Rotated Rosenbrock’s Function\n")

    for mprobability in mutation_probabilities:
        for mrate in mutation_rates:
            time1 = time.time()
            results = np.array([SLC(f4, dim=dim, max_eval=evaluations, nteams=teams,
                nmain=main_players, nsubs=sub_players, mutation_probability=mprobability,
                mutation_rate=mrate, lower_bound=-100, upper_bound=100) for _ in range(repeats)])
            total_time = time.time() - time1
            print("Mutation probability: {}\tMutation rate: {}".format(mprobability, mrate))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")

    print("###############################################")

    np.random.seed(10)

    def f17(x):
        return cec2014.cec14(x,17)
    
    print("F17: Hybrid Function 1 (N=3)\n")

    for mprobability in mutation_probabilities:
        for mrate in mutation_rates:
            time1 = time.time()
            results = np.array([SLC(f17, dim=dim, max_eval=evaluations, nteams=teams,
                nmain=main_players, nsubs=sub_players, mutation_probability=mprobability,
                mutation_rate=mrate, lower_bound=-100, upper_bound=100) for _ in range(repeats)])
            total_time = time.time() - time1
            print("Mutation probability: {}\tMutation rate: {}".format(mprobability, mrate))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")

    print("###############################################")

    np.random.seed(10)

    def f23(x):
        return cec2014.cec14(x,23)
    
    print("F23: Composition Function 1 (N=5)\n")

    for mprobability in mutation_probabilities:
        for mrate in mutation_rates:
            time1 = time.time()
            results = np.array([SLC(f23, dim=dim, max_eval=evaluations, nteams=teams,
                nmain=main_players, nsubs=sub_players, mutation_probability=mprobability,
                mutation_rate=mrate, lower_bound=-5, upper_bound=5) for _ in range(repeats)])
            total_time = time.time() - time1
            print("Mutation probability: {}\tMutation rate: {}".format(mprobability, mrate))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")