import optproblems.cec2005
import numpy as np
import time
from ASO import *
import os

if __name__ == "__main__":
    dim = 30
    repeats = 10
    evaluations = 10000*dim
    population = 30
    external_rate = 3
    internal_rate = 1
    fickleness_rate = 0.5

    if not os.path.exists('results'):
        os.makedirs('results')

    if not os.path.exists('convergence'):
        os.makedirs('convergence')

    np.random.seed(10)

    f4 = optproblems.cec2005.F4(dim)

    time1 = time.time()
    results = np.array([ASO(f4, dim=dim, max_eval=evaluations, external_rate=external_rate,
        internal_rate=internal_rate, lower_bound=-100, upper_bound=100,
        fickleness_rate=fickleness_rate) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/ASO-results-30-4.txt", "w") as file:
        print("F4: Shifted Schwefel's Problem 1.2 with Noise in Fitness", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)

    with open("convergence/ASO-convergence-30-4.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)   
    
    f9 = optproblems.cec2005.F9(dim)

    time1 = time.time()
    results = np.array([ASO(f9, dim=dim, max_eval=evaluations, external_rate=external_rate,
        internal_rate=internal_rate, lower_bound=-5, upper_bound=5,
        fickleness_rate=fickleness_rate) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/ASO-results-30-9.txt", "w") as file:
        print("F9: Shifted Rastrigin's Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/ASO-convergence-30-9.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f12 = optproblems.cec2005.F12(dim)

    time1 = time.time()
    results = np.array([ASO(f12, dim=dim, max_eval=evaluations, external_rate=external_rate,
        internal_rate=internal_rate, lower_bound=-np.pi, upper_bound=np.pi,
        fickleness_rate=fickleness_rate) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/ASO-results-30-12.txt", "w") as file:
        print("F12: Schwefel's Problem 2.13", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/ASO-convergence-30-12.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f21 = optproblems.cec2005.F21(dim)

    time1 = time.time()
    results = np.array([ASO(f21, dim=dim, max_eval=evaluations, external_rate=external_rate,
        internal_rate=internal_rate, lower_bound=-5, upper_bound=5,
        fickleness_rate=fickleness_rate) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/ASO-results-30-21.txt", "w") as file:
        print("F21: Rotated Hybrid Composition Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/ASO-convergence-30-21.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f22 = optproblems.cec2005.F22(dim)

    time1 = time.time()
    results = np.array([ASO(f22, dim=dim, max_eval=evaluations, external_rate=external_rate,
        internal_rate=internal_rate, lower_bound=-5, upper_bound=5,
        fickleness_rate=fickleness_rate) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/ASO-results-30-22.txt", "w") as file:
        print("F22: Rotated Hybrid Composition Function with High Condition Number Matrix", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/ASO-convergence-30-22.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)
