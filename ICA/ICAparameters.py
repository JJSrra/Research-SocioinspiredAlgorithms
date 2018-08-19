import optproblems.cec2005
import numpy as np
import time
from ICA import *

if __name__ == "__main__":
    dim = 10
    repeats = 10
    evaluations = 10000*dim
    countries = 30
    imperialists_list = [3,4,5,6]
    revolution_rates = [0.2,0.3,0.4]

    f1 = optproblems.cec2005.F1(dim)
    print("F1: Shifted Sphere Function\n")

    for imperialists in imperialists_list:
        for revolution_rate in revolution_rates:
            time1 = time.time()
            results = np.array([ICA(f1, dim=dim, evaluation_criteria=True, max_eval=evaluations,
                ncountries=countries, nimperialists=imperialists, revolution_rate=revolution_rate,
                lower_bound=-100, upper_bound=100) for _ in range(repeats)])
            total_time = time.time() - time1
            print("Imperialists: {}\tRevolution rate: {}".format(imperialists, revolution_rate))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")

    print("###############################################")
    
    f6 = optproblems.cec2005.F6(dim)
    print("F6: Shifted Rosenbrock’s Function\n")

    for imperialists in imperialists_list:
        for revolution_rate in revolution_rates:
            time1 = time.time()
            results = np.array([ICA(f6, dim=dim, evaluation_criteria=True, max_eval=evaluations,
                ncountries=countries, nimperialists=imperialists, revolution_rate=revolution_rate,
                lower_bound=-100, upper_bound=100) for _ in range(repeats)])
            total_time = time.time() - time1
            print("Imperialists: {}\tRevolution rate: {}".format(imperialists, revolution_rate))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")

    print("###############################################")

    f14 = optproblems.cec2005.F14(dim)
    print("F14: Shifted Rotated Expanded Scaffer’s F6\n")

    for imperialists in imperialists_list:
        for revolution_rate in revolution_rates:
            time1 = time.time()
            results = np.array([ICA(f14, dim=dim, evaluation_criteria=True, max_eval=evaluations,
                ncountries=countries, nimperialists=imperialists, revolution_rate=revolution_rate,
                lower_bound=-100, upper_bound=100) for _ in range(repeats)])
            total_time = time.time() - time1
            print("Imperialists: {}\tRevolution rate: {}".format(imperialists, revolution_rate))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")

    print("###############################################")

    f15 = optproblems.cec2005.F15(dim)
    print("F15: Hybrid Composition Function\n")

    for imperialists in imperialists_list:
        for revolution_rate in revolution_rates:
            time1 = time.time()
            results = np.array([ICA(f1, dim=dim, evaluation_criteria=True, max_eval=evaluations,
                ncountries=countries, nimperialists=imperialists, revolution_rate=revolution_rate,
                lower_bound=-5, upper_bound=5) for _ in range(repeats)])
            total_time = time.time() - time1
            print("Imperialists: {}\tRevolution rate: {}".format(imperialists, revolution_rate))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")
