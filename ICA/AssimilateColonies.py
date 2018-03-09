import numpy as np
import numpy.matlib

def AssimilateColonies(imperialist, colonies, domain, assimilation_coef, CostFunction):
    lower_bound, upper_bound = domain

    # The imperialist position will have an impact in any colony movement
    vector = np.matlib.repmat(imperialist, len(colonies), 1) - colonies

    # The multiplier helps searching different points around the imperialist
    multiplier = np.random.rand(len(vector)).reshape(len(vector), 1)

    # And finally we calculate each colony's new position, and clip the values according to the domain
    colonies = colonies + 2 * assimilation_coef * multiplier * vector
    colonies = np.clip(colonies, lower_bound, upper_bound)

    colonies_fitness = np.apply_along_axis(CostFunction, 1, colonies);


    return colonies, colonies_fitness
