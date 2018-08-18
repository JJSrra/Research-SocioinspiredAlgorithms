import optproblems.cec2005
import numpy as np
import time
from POA import *

if __name__ == "__main__":
    dim = 10
    repeats = 10
    evaluations = 10000*dim
    parties = 5
    members = 6
    candidates_list = [1,2,3]

    f1 = optproblems.cec2005.F1(dim)
    print("F1: Shifted Sphere Function\n")

    for candidates in candidates_list:
        time1 = time.time()
        results = np.array([POA(f1, dim=dim, max_eval=evaluations, nparties=parties,
            nmembers=members, lower_bound=-100, upper_bound=100) for _ in range(repeats)])
        total_time = time.time() - time1
        print("Candidates: {}".format(candidates))
        print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
        print("_______________________________________________")

    print("###############################################")

    f6 = optproblems.cec2005.F6(dim)
    print("F6: Shifted Rosenbrock’s Function\n")

    for candidates in candidates_list:
        time1 = time.time()
        results = np.array([POA(f6, dim=dim, max_eval=evaluations, nparties=parties,
            nmembers=members, lower_bound=-100, upper_bound=100) for _ in range(repeats)])
        total_time = time.time() - time1
        print("Candidates: {}".format(candidates))
        print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
        print("_______________________________________________")

    print("###############################################")

    f14 = optproblems.cec2005.F14(dim)
    print("F14: Shifted Rotated Expanded Scaffer’s F6\n")

    for candidates in candidates_list:
        time1 = time.time()
        results = np.array([POA(f14, dim=dim, max_eval=evaluations, nparties=parties,
            nmembers=members, lower_bound=-100, upper_bound=100) for _ in range(repeats)])
        total_time = time.time() - time1
        print("Candidates: {}".format(candidates))
        print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
        print("_______________________________________________")

    print("###############################################")

    f15 = optproblems.cec2005.F15(dim)
    print("F15: Hybrid Composition Function\n")

    for candidates in candidates_list:
        time1 = time.time()
        results = np.array([POA(f15, dim=dim, max_eval=evaluations, nparties=parties,
            nmembers=members, lower_bound=-5, upper_bound=5) for _ in range(repeats)])
        total_time = time.time() - time1
        print("Candidates: {}".format(candidates))
        print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
        print("_______________________________________________")
