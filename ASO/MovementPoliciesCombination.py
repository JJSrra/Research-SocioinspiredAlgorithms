import numpy as np

def SelectBestPosition(CostFunction, current_policy, society_policy, previous_policy):
    dim = len(current_policy)
    policies = np.concatenate((current_policy, society_policy, previous_policy)).reshape(3,dim)
    policies_fitness = np.apply_along_axis(CostFunction, 1, policies)
    
    best = np.argsort(policies_fitness)[0]
    return policies[best], policies_fitness[best]