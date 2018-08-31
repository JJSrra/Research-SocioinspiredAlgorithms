import cec2014
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

    def f1(x):
        return cec2014.cec14(x,1)
    
    print("F1: Rotated High Conditioned Elliptic Function\n")

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

    def f4(x):
        return cec2014.cec14(x,4)
    
    print("F4: Shifted and Rotated Rosenbrock’s Function\n")

    for external_rate in external_rates:
        for internal_rate in internal_rates:
            for fickleness_rate in fickleness_rates:
                time1 = time.time()
                results = np.array([ASO(f4, dim=dim, max_eval=evaluations, external_rate=external_rate,
                    internal_rate=internal_rate, lower_bound=-100, upper_bound=100, fickleness_rate=fickleness_rate) for _ in range(repeats)])
                total_time = time.time() - time1
                print("External rate: {}\tInternal rate: {}\tFickleness rate: {}".format(external_rate, internal_rate, fickleness_rate))
                print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
                print("_______________________________________________")

    print("###############################################")

    np.random.seed(10)

    def f17(x):
        return cec2014.cec14(x,17)
    
    print("F17: Hybrid Function 1 (N=3)\n")

    for external_rate in external_rates:
        for internal_rate in internal_rates:
            for fickleness_rate in fickleness_rates:
                time1 = time.time()
                results = np.array([ASO(f17, dim=dim, max_eval=evaluations, external_rate=external_rate,
                    internal_rate=internal_rate, lower_bound=-100, upper_bound=100, fickleness_rate=fickleness_rate) for _ in range(repeats)])
                total_time = time.time() - time1
                print("External rate: {}\tInternal rate: {}\tFickleness rate: {}".format(external_rate, internal_rate, fickleness_rate))
                print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
                print("_______________________________________________")

    print("###############################################")

    np.random.seed(10)

    def f23(x):
        return cec2014.cec14(x,23)
    
    print("F23: Composition Function 1 (N=5)\n")

    for external_rate in external_rates:
        for internal_rate in internal_rates:
            for fickleness_rate in fickleness_rates:
                time1 = time.time()
                results = np.array([ASO(f23, dim=dim, max_eval=evaluations, external_rate=external_rate,
                    internal_rate=internal_rate, lower_bound=-5, upper_bound=5, fickleness_rate=fickleness_rate) for _ in range(repeats)])
                total_time = time.time() - time1
                print("External rate: {}\tInternal rate: {}\tFickleness rate: {}".format(external_rate, internal_rate, fickleness_rate))
                print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
                print("_______________________________________________")