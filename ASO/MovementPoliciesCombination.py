import numpy as np

def SelectBestPolicy(CostFunction, current_policy, society_policy, previous_policy):
    dim = len(current_policy)
    policies = np.concatenate((current_policy, society_policy, previous_policy)).reshape(3,dim)
    policies_fitness = np.apply_along_axis(CostFunction, 1, policies)
    
    best = np.argsort(policies_fitness)[0]
    return np.append(policies_fitness[best], policies[best])

def NewPositionsPolicyBased(CostFunction, current_policies, society_policies, previous_policies):
    results = np.array([SelectBestPolicy(CostFunction, current, society, previous)
			for (current, society, previous) in zip(current_policies, society_policies, previous_policies)])

    new_fitness = results[:, 0]
    new_positions = np.delete(results, 0, 1)

    return new_positions, new_fitness