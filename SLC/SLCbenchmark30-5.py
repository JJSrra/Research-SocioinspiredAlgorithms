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

    f5 = optproblems.cec2005.F5(dim)

    time1 = time.time()
    results = np.array([SLC(f5, dim=dim, max_eval=evaluations, nteams=teams,
        nmain=main_players, nsubs=sub_players, mutation_probability=mutation_probability,
        mutation_rate=mutation_rate, lower_bound=-100, upper_bound=100) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SLC-resultsd-30-5.txt", "w") as file:
        print("F5: Schwefel's Problem 2.6 with Global Optimum on Bounds", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)

    with open("convergence/SLC-convergenced-30-5.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)   
    
    f10 = optproblems.cec2005.F10(dim)

    time1 = time.time()
    results = np.array([SLC(f10, dim=dim, max_eval=evaluations, nteams=teams,
        nmain=main_players, nsubs=sub_players, mutation_probability=mutation_probability,
        mutation_rate=mutation_rate, lower_bound=-5, upper_bound=5) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SLC-resultsd-30-10.txt", "w") as file:
        print("F10: Shifted Rotated Rastrigin's Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SLC-convergenced-30-10.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f23 = optproblems.cec2005.F23(dim)

    time1 = time.time()
    results = np.array([SLC(f23, dim=dim, max_eval=evaluations, nteams=teams,
        nmain=main_players, nsubs=sub_players, mutation_probability=mutation_probability,
        mutation_rate=mutation_rate, lower_bound=-np.pi, upper_bound=np.pi) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SLC-resultsd-30-23.txt", "w") as file:
        print("F23: Non-Continuous Rotated Hybrid Composition Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SLC-convergenced-30-23.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f24 = optproblems.cec2005.F24(dim)

    time1 = time.time()
    results = np.array([SLC(f24, dim=dim, max_eval=evaluations, nteams=teams,
        nmain=main_players, nsubs=sub_players, mutation_probability=mutation_probability,
        mutation_rate=mutation_rate, lower_bound=-5, upper_bound=5) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SLC-resultsd-30-24.txt", "w") as file:
        print("F24: Rotated Hybrid Composition Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SLC-convergenced-30-24.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f25 = optproblems.cec2005.F25(dim)

    time1 = time.time()
    results = np.array([SLC(f25, dim=dim, max_eval=evaluations, nteams=teams,
        nmain=main_players, nsubs=sub_players, mutation_probability=mutation_probability,
        mutation_rate=mutation_rate, lower_bound=-999999, upper_bound=999999) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SLC-resultsd-30-25.txt", "w") as file:
        print("F25: Rotated Hybrid Composition Function without Bounds", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SLC-convergenced-30-25.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)
