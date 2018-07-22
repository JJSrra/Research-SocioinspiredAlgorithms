import numpy as np

def Manner1(individual, population, k1):
    return -k1 * np.random.uniform(0,1) * np.sum(population - individual, 0)

def Manner2(individual, status_best, k2):
    return k2 * np.random.uniform(0,1) * (status_best - individual)

def Manner3Aux(individual, individual_best, k3):
    return k3 * np.random.uniform(0,1) * (individual_best - individual)

def Manner3(individual, individual_best, status_best, population, k1, k2, k3):
    manner3 = Manner3Aux(individual, individual_best, k3)
    manner2 = Manner2(individual, status_best, k2)
    manner1 = Manner1(individual, population, k1)

    return manner3 + manner2 + manner1

def Manner4(individual, individual_best, population, k1, k3):
    manner3 = Manner3Aux(individual, individual_best, k3)
    manner1 = Manner1(individual, population, k1)

    return manner3 + manner1
