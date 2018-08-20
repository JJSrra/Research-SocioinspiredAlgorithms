import optproblems.cec2005
import numpy as np
import time
from ASO import *

if __name__ == "__main__":
    dim = 10
    repeats = 10
    evaluations = 10000*dim
    population = 30
    external_rates = [1,2,3,4]
    internal_rates = [1,2,3,4]
    fickleness_rates = [0.3, 0.5, 0.7]

    np.random.seed(10)

    f1 = optproblems.cec2005.F1(dim)
    print("F1: Shifted Sphere Function\n")

    for external_rate in external_rates:
        for internal_rate in internal_rates:
            for fickleness_rate in fickleness_rates:
                time1 = time.time()
                results = np.array([ASO(f1, dim=dim, max_eval=evaluations, external_rate=external_rate,
                    internal_rate=internal_rate, lower_bound=-100, upper_bound=100, fickleness_rate=fickleness_rate) for _ in range(repeats)])
                total_time = time.time() - time1
                print("External rate: {}\tInternal rate: {}\tFickleness rate: {}".format(external_rate, internal_rate, fickleness_rate))
                print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
                print("_______________________________________________")
    
    print("###############################################")

    np.random.seed(10)

    f6 = optproblems.cec2005.F6(dim)
    print("F6: Shifted Rosenbrock’s Function\n")

    for external_rate in external_rates:
        for internal_rate in internal_rates:
            for fickleness_rate in fickleness_rates:
                time1 = time.time()
                results = np.array([ASO(f6, dim=dim, max_eval=evaluations, external_rate=external_rate,
                    internal_rate=internal_rate, lower_bound=-100, upper_bound=100, fickleness_rate=fickleness_rate) for _ in range(repeats)])
                total_time = time.time() - time1
                print("External rate: {}\tInternal rate: {}\tFickleness rate: {}".format(external_rate, internal_rate, fickleness_rate))
                print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
                print("_______________________________________________")

    print("###############################################")

    np.random.seed(10)

    f14 = optproblems.cec2005.F14(dim)
    print("F14: Shifted Rotated Expanded Scaffer’s F6\n")

    for external_rate in external_rates:
        for internal_rate in internal_rates:
            for fickleness_rate in fickleness_rates:
                time1 = time.time()
                results = np.array([ASO(f14, dim=dim, max_eval=evaluations, external_rate=external_rate,
                    internal_rate=internal_rate, lower_bound=-100, upper_bound=100, fickleness_rate=fickleness_rate) for _ in range(repeats)])
                total_time = time.time() - time1
                print("External rate: {}\tInternal rate: {}\tFickleness rate: {}".format(external_rate, internal_rate, fickleness_rate))
                print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
                print("_______________________________________________")

    print("###############################################")

    np.random.seed(10)

    f15 = optproblems.cec2005.F15(dim)
    print("F15: Hybrid Composition Function\n")

    for external_rate in external_rates:
        for internal_rate in internal_rates:
            for fickleness_rate in fickleness_rates:
                time1 = time.time()
                results = np.array([ASO(f15, dim=dim, max_eval=evaluations, external_rate=external_rate,
                    internal_rate=internal_rate, lower_bound=-5, upper_bound=5, fickleness_rate=fickleness_rate) for _ in range(repeats)])
                total_time = time.time() - time1
                print("External rate: {}\tInternal rate: {}\tFickleness rate: {}".format(external_rate, internal_rate, fickleness_rate))
                print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
                print("_______________________________________________")