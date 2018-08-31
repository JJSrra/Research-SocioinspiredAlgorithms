import optproblems.cec2005
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

    f1 = optproblems.cec2005.F1(dim)
    print("F1: Shifted Sphere Function\n")

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

    f6 = optproblems.cec2005.F6(dim)
    print("F6: Shifted Rosenbrock’s Function\n")

    for k1 in k1_list:
        for k2 in k2_list:
            for k3 in k3_list:
                time1 = time.time()
                results = np.array([SEA(f6, dim=dim, max_eval=evaluations,
                    nindividuals=individuals, k1=k1, k2=k2, k3=k3,
                    lower_bound=-100, upper_bound=100) for _ in range(repeats)])
                total_time = time.time() - time1
                print("k1: {}\tk2: {}\tk3: {}".format(k1, k2, k3))
                print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
                print("_______________________________________________")

    print("###############################################")

    np.random.seed(10)

    f14 = optproblems.cec2005.F14(dim)
    print("F14: Shifted Rotated Expanded Scaffer’s F6\n")

    for k1 in k1_list:
        for k2 in k2_list:
            for k3 in k3_list:
                time1 = time.time()
                results = np.array([SEA(f14, dim=dim, max_eval=evaluations,
                    nindividuals=individuals, k1=k1, k2=k2, k3=k3,
                    lower_bound=-100, upper_bound=100) for _ in range(repeats)])
                total_time = time.time() - time1
                print("k1: {}\tk2: {}\tk3: {}".format(k1, k2, k3))
                print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
                print("_______________________________________________")

    print("###############################################")

    np.random.seed(10)

    f15 = optproblems.cec2005.F15(dim)
    print("F15: Hybrid Composition Function\n")

    for k1 in k1_list:
        for k2 in k2_list:
            for k3 in k3_list:
                time1 = time.time()
                results = np.array([SEA(f15, dim=dim, max_eval=evaluations,
                    nindividuals=individuals, k1=k1, k2=k2, k3=k3,
                    lower_bound=-5, upper_bound=5) for _ in range(repeats)])
                total_time = time.time() - time1
                print("k1: {}\tk2: {}\tk3: {}".format(k1, k2, k3))
                print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
                print("_______________________________________________")

