import cec2014
import numpy as np
import time
from SEA import *

if __name__ == "__main__":
    dim = 10
    repeats = 10
    evaluations = 10000*dim
    individuals = 30
    k1_list = [0.1,0.2,0.3,0.4]
    k2_list = [0.1,0.2,0.3,0.4]
    k3_list = [0.1,0.2,0.3,0.4]

    np.random.seed(10)

    def f1(x):
        return cec2014.cec14(x,1)
    
    print("F1: Rotated High Conditioned Elliptic Function\n")

    for k1 in k1_list:
        for k2 in k2_list:
            for k3 in k3_list:
                time1 = time.time()
                results = np.array([SEA(f1, dim=dim, max_eval=evaluations,
                    nindividuals=individuals, k1=k1, k2=k2, k3=k3,
                    lower_bound=-100, upper_bound=100) for _ in range(repeats)])
                total_time = time.time() - time1
                print("k1: {}\tk2: {}\tk3: {}".format(k1, k2, k3))
                print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
                print("_______________________________________________")

    print("###############################################")

    np.random.seed(10)

    def f4(x):
        return cec2014.cec14(x,4)
    
    print("F4: Shifted and Rotated Rosenbrock’s Function\n")

    for k1 in k1_list:
        for k2 in k2_list:
            for k3 in k3_list:
                time1 = time.time()
                results = np.array([SEA(f4, dim=dim, max_eval=evaluations,
                    nindividuals=individuals, k1=k1, k2=k2, k3=k3,
                    lower_bound=-100, upper_bound=100) for _ in range(repeats)])
                total_time = time.time() - time1
                print("k1: {}\tk2: {}\tk3: {}".format(k1, k2, k3))
                print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
                print("_______________________________________________")

    print("###############################################")

    np.random.seed(10)

    def f17(x):
        return cec2014.cec14(x,17)
    
    print("F17: Hybrid Function 1 (N=3)\n")

    for k1 in k1_list:
        for k2 in k2_list:
            for k3 in k3_list:
                time1 = time.time()
                results = np.array([SEA(f17, dim=dim, max_eval=evaluations,
                    nindividuals=individuals, k1=k1, k2=k2, k3=k3,
                    lower_bound=-100, upper_bound=100) for _ in range(repeats)])
                total_time = time.time() - time1
                print("k1: {}\tk2: {}\tk3: {}".format(k1, k2, k3))
                print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
                print("_______________________________________________")

    print("###############################################")

    np.random.seed(10)

    def f23(x):
        return cec2014.cec14(x,23)
    
    print("F23: Composition Function 1 (N=5)\n")

    for k1 in k1_list:
        for k2 in k2_list:
            for k3 in k3_list:
                time1 = time.time()
                results = np.array([SEA(f23, dim=dim, max_eval=evaluations,
                    nindividuals=individuals, k1=k1, k2=k2, k3=k3,
                    lower_bound=-5, upper_bound=5) for _ in range(repeats)])
                total_time = time.time() - time1
                print("k1: {}\tk2: {}\tk3: {}".format(k1, k2, k3))
                print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
                print("_______________________________________________")

