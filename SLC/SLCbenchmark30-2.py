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

    f2 = optproblems.cec2005.F2(dim)

    time1 = time.time()
    results = np.array([SLC(f2, dim=dim, max_eval=evaluations, nteams=teams,
        nmain=main_players, nsubs=sub_players, mutation_probability=mutation_probability,
        mutation_rate=mutation_rate, lower_bound=-100, upper_bound=100) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SLC-results-30-2.txt", "w") as file:
        print("F2: Shifted Schwefel's Problem 1.2", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)

    with open("convergence/SLC-convergence-30-2.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)   
    
    f7 = optproblems.cec2005.F7(dim)

    time1 = time.time()
    results = np.array([SLC(f7, dim=dim, max_eval=evaluations, nteams=teams,
        nmain=main_players, nsubs=sub_players, mutation_probability=mutation_probability,
        mutation_rate=mutation_rate, lower_bound=-999999, upper_bound=999999) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SLC-results-30-7.txt", "w") as file:
        print("F7: Shifted Rotated Griewank's Function without Bounds", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SLC-convergence-30-7.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f13 = optproblems.cec2005.F13(dim)

    time1 = time.time()
    results = np.array([SLC(f13, dim=dim, max_eval=evaluations, nteams=teams,
        nmain=main_players, nsubs=sub_players, mutation_probability=mutation_probability,
        mutation_rate=mutation_rate, lower_bound=-3, upper_bound=1) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SLC-results-30-13.txt", "w") as file:
        print("F13: Expanded Extended Griewank's plus Rosenbrock's Function (F8F2)", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SLC-convergence-30-13.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f17 = optproblems.cec2005.F17(dim)

    time1 = time.time()
    results = np.array([SLC(f17, dim=dim, max_eval=evaluations, nteams=teams,
        nmain=main_players, nsubs=sub_players, mutation_probability=mutation_probability,
        mutation_rate=mutation_rate, lower_bound=-5, upper_bound=5) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SLC-results-30-17.txt", "w") as file:
        print("F17: Rotated Hybrid Composition Function with Noise in Fitness", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SLC-convergence-30-17.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f18 = optproblems.cec2005.F18(dim)

    time1 = time.time()
    results = np.array([SLC(f18, dim=dim, max_eval=evaluations, nteams=teams,
        nmain=main_players, nsubs=sub_players, mutation_probability=mutation_probability,
        mutation_rate=mutation_rate, lower_bound=-5, upper_bound=5) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SLC-results-30-18.txt", "w") as file:
        print("F18: Rotated Hybrid Composition Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SLC-convergence-30-18.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)
