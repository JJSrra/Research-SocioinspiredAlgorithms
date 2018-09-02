import optproblems.cec2005
import numpy as np
import time
from SEA import *
import os

if __name__ == "__main__":
    dim = 10
    repeats = 1
    evaluations = 10000*dim
    individuals = 30
    k1 = 0.1
    k2 = 0.4
    k3 = 0.4

    if not os.path.exists('results'):
        os.makedirs('results')

    if not os.path.exists('convergence'):
        os.makedirs('convergence')

    
    np.random.seed(10)

    f25 = optproblems.cec2005.F25(dim)

    time1 = time.time()
    results = np.array([SEA(f25, dim=dim, max_eval=evaluations,
        nindividuals=individuals, k1=k1, k2=k2, k3=k3,
        lower_bound=-10, upper_bound=10, initial_population_lower_bound=2,
        initial_population_upper_bound=5) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SEA-results-10-25.txt", "w") as file:
        print("F25: Rotated Hybrid Composition Function without Bounds", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SEA-convergence-10-25.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)
