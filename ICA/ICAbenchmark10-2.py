import optproblems.cec2005
import numpy as np
import time
from ICA import *
import os

if __name__ == "__main__":
    dim = 10
    repeats = 10
    evaluations = 10000*dim
    countries = 30
    imperialists = 6

    if not os.path.exists('results'):
        os.makedirs('results')

    if not os.path.exists('convergence'):
        os.makedirs('convergence')

    np.random.seed(10)

    f2 = optproblems.cec2005.F2(dim)

    time1 = time.time()
    results = np.array([ICA(f2, dim=dim, evaluation_criteria=True,
        max_eval=evaluations, ncountries=countries, nimperialists=imperialists,
        lower_bound=-100, upper_bound=100) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/ICA-results-10-2.txt", "w") as file:
        print("F2: Shifted Schwefel's Problem 1.2", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)

    with open("convergence/ICA-convergence-10-2.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)   
    
    f7 = optproblems.cec2005.F7(dim)

    time1 = time.time()
    results = np.array([ICA(f7, dim=dim, evaluation_criteria=True,
        max_eval=evaluations, ncountries=countries, nimperialists=imperialists,
        lower_bound=-999999, upper_bound=999999, initial_population_lower_bound=0,
        initial_population_upper_bound=600) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/ICA-results-10-7.txt", "w") as file:
        print("F7: Shifted Rotated Griewank's Function without Bounds", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/ICA-convergence-10-7.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f13 = optproblems.cec2005.F13(dim)

    time1 = time.time()
    results = np.array([ICA(f13, dim=dim, evaluation_criteria=True,
        max_eval=evaluations, ncountries=countries, nimperialists=imperialists,
        lower_bound=-3, upper_bound=1) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/ICA-results-10-13.txt", "w") as file:
        print("F13: Expanded Extended Griewank's plus Rosenbrock's Function (F8F2)", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/ICA-convergence-10-13.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f17 = optproblems.cec2005.F17(dim)

    time1 = time.time()
    results = np.array([ICA(f17, dim=dim, evaluation_criteria=True,
        max_eval=evaluations, ncountries=countries, nimperialists=imperialists,
        lower_bound=-5, upper_bound=5) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/ICA-results-10-17.txt", "w") as file:
        print("F17: Rotated Hybrid Composition Function with Noise in Fitness", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/ICA-convergence-10-17.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f18 = optproblems.cec2005.F18(dim)

    time1 = time.time()
    results = np.array([ICA(f18, dim=dim, evaluation_criteria=True,
        max_eval=evaluations, ncountries=countries, nimperialists=imperialists,
        lower_bound=-5, upper_bound=5) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/ICA-results-10-18.txt", "w") as file:
        print("F18: Rotated Hybrid Composition Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/ICA-convergence-10-18.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)
