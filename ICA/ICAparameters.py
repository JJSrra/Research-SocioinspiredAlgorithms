import cec2014
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

    np.random.seed(10)

    def f1(x):
        return cec2014.cec14(x,1)
    
    print("F1: Rotated High Conditioned Elliptic Function\n")

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

    np.random.seed(10)   
    
    def f4(x):
        return cec2014.cec14(x,4)
    
    print("F4: Shifted and Rotated Rosenbrock’s Function\n")

    for imperialists in imperialists_list:
        for revolution_rate in revolution_rates:
            time1 = time.time()
            results = np.array([ICA(f4, dim=dim, evaluation_criteria=True, max_eval=evaluations,
                ncountries=countries, nimperialists=imperialists, revolution_rate=revolution_rate,
                lower_bound=-100, upper_bound=100) for _ in range(repeats)])
            total_time = time.time() - time1
            print("Imperialists: {}\tRevolution rate: {}".format(imperialists, revolution_rate))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")

    print("###############################################")

    np.random.seed(10)

    def f17(x):
        return cec2014.cec14(x,17)
    
    print("F17: Hybrid Function 1 (N=3)\n")

    for imperialists in imperialists_list:
        for revolution_rate in revolution_rates:
            time1 = time.time()
            results = np.array([ICA(f17, dim=dim, evaluation_criteria=True, max_eval=evaluations,
                ncountries=countries, nimperialists=imperialists, revolution_rate=revolution_rate,
                lower_bound=-100, upper_bound=100) for _ in range(repeats)])
            total_time = time.time() - time1
            print("Imperialists: {}\tRevolution rate: {}".format(imperialists, revolution_rate))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")

    print("###############################################")

    np.random.seed(10)

    def f23(x):
        return cec2014.cec14(x,23)
    
    print("F23: Composition Function 1 (N=5)\n")

    for imperialists in imperialists_list:
        for revolution_rate in revolution_rates:
            time1 = time.time()
            results = np.array([ICA(f23, dim=dim, evaluation_criteria=True, max_eval=evaluations,
                ncountries=countries, nimperialists=imperialists, revolution_rate=revolution_rate,
                lower_bound=-5, upper_bound=5) for _ in range(repeats)])
            total_time = time.time() - time1
            print("Imperialists: {}\tRevolution rate: {}".format(imperialists, revolution_rate))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")
