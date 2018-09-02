import optproblems.cec2005
import numpy as np
import time
from SEA import *
import os

if __name__ == "__main__":
    dim = 30
    repeats = 10
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

    f3 = optproblems.cec2005.F3(dim)

    time1 = time.time()
    results = np.array([SEA(f3, dim=dim, max_eval=evaluations,
        nindividuals=individuals, k1=k1, k2=k2, k3=k3,
        lower_bound=-100, upper_bound=100) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SEA-results-30-3.txt", "w") as file:
        print("F3: Shifted Rotated High Conditioned Elliptic Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)

    with open("convergence/SEA-convergence-30-3.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)   
    
    f8 = optproblems.cec2005.F8(dim)

    time1 = time.time()
    results = np.array([SEA(f8, dim=dim, max_eval=evaluations,
        nindividuals=individuals, k1=k1, k2=k2, k3=k3,
        lower_bound=-32, upper_bound=32) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SEA-results-30-8.txt", "w") as file:
        print("F8: Shifted Rotated Ackley's Function with Global Optimum on Bounds", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SEA-convergence-30-8.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f11 = optproblems.cec2005.F11(dim)

    time1 = time.time()
    results = np.array([SEA(f11, dim=dim, max_eval=evaluations,
        nindividuals=individuals, k1=k1, k2=k2, k3=k3,
        lower_bound=-0.5, upper_bound=0.5) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SEA-results-30-11.txt", "w") as file:
        print("F11: Shifted Rotated Weierstrass Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SEA-convergence-30-11.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f19 = optproblems.cec2005.F19(dim)

    time1 = time.time()
    results = np.array([SEA(f19, dim=dim, max_eval=evaluations,
        nindividuals=individuals, k1=k1, k2=k2, k3=k3,
        lower_bound=-19, upper_bound=19) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SEA-results-30-19.txt", "w") as file:
        print("F19: Rotated Hybrid Composition Function with a Narrow Basin for the Global Optimum", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SEA-convergence-30-19.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f20 = optproblems.cec2005.F20(dim)

    time1 = time.time()
    results = np.array([SEA(f20, dim=dim, max_eval=evaluations,
        nindividuals=individuals, k1=k1, k2=k2, k3=k3,
        lower_bound=-5, upper_bound=5) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SEA-results-30-20.txt", "w") as file:
        print("F20: Rotated Hybrid Composition Function with the Global Optimum on the Bounds", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SEA-convergence-30-20.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)
