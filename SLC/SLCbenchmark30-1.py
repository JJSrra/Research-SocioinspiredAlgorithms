import optproblems.cec2005
import numpy as np
import time
from SLC import *
import os

if __name__ == "__main__":
    dim = 30
    repeats = 10
    evaluations = 10000*dim
    teams = 5
    main_players = 3
    sub_players = 3
    mutation_probability = 0.1
    mutation_rate = 0.2

    if not os.path.exists('results'):
        os.makedirs('results')

    if not os.path.exists('convergence'):
        os.makedirs('convergence')

    np.random.seed(10)

    f1 = optproblems.cec2005.F1(dim)

    time1 = time.time()
    results = np.array([SLC(f1, dim=dim, max_eval=evaluations, nteams=teams,
        nmain=main_players, nsubs=sub_players, mutation_probability=mutation_probability,
        mutation_rate=mutation_rate, lower_bound=-100, upper_bound=100) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SLC-results-30-1.txt", "w") as file:
        print("F1: Shifted Sphere Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SLC-convergence-30-1.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)


    np.random.seed(10)   
    
    f6 = optproblems.cec2005.F6(dim)

    time1 = time.time()
    results = np.array([SLC(f6, dim=dim, max_eval=evaluations, nteams=teams,
        nmain=main_players, nsubs=sub_players, mutation_probability=mutation_probability,
        mutation_rate=mutation_rate, lower_bound=-100, upper_bound=100) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SLC-results-30-6.txt", "w") as file:
        print("F6: Shifted Rosenbrock's Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SLC-convergence-30-6.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f14 = optproblems.cec2005.F14(dim)

    time1 = time.time()
    results = np.array([SLC(f14, dim=dim, max_eval=evaluations, nteams=teams,
        nmain=main_players, nsubs=sub_players, mutation_probability=mutation_probability,
        mutation_rate=mutation_rate, lower_bound=-100, upper_bound=100) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SLC-results-30-14.txt", "w") as file:
        print("F14: Shifted Rotated Expanded Scaffer's F6", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SLC-convergence-30-14.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f15 = optproblems.cec2005.F15(dim)

    time1 = time.time()
    results = np.array([SLC(f15, dim=dim, max_eval=evaluations, nteams=teams,
        nmain=main_players, nsubs=sub_players, mutation_probability=mutation_probability,
        mutation_rate=mutation_rate, lower_bound=-5, upper_bound=5) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SLC-results-30-15.txt", "w") as file:
        print("F15: Hybrid Composition Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SLC-convergence-30-15.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f16 = optproblems.cec2005.F16(dim)

    time1 = time.time()
    results = np.array([SLC(f16, dim=dim, max_eval=evaluations, nteams=teams,
        nmain=main_players, nsubs=sub_players, mutation_probability=mutation_probability,
        mutation_rate=mutation_rate, lower_bound=-5, upper_bound=5) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SLC-results-30-16.txt", "w") as file:
        print("F16: Rotated Hybrid Composition Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SLC-convergence-30-16.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)
