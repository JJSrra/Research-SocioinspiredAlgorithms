import numpy as np
import numpy.matlib

def AssimilateColonies(empire, domain, assimilation_coef):
    lower_bound, upper_bound = domain

    # We need to separate the imperialist to get the number of colonies
    colonies = empire[1:len(empire)]

    # The imperialist position will have an impact in any colony movement
    vector = np.matlib.repmat(empire[0], len(colonies), 1) - colonies

    # The multiplier helps searching different points around the imperialist
    multiplier = np.random.rand(len(vector)).reshape(len(vector), 1)

    # And finally we calculate each colony's new position, and clip the values according to the domain
    colonies = colonies + 2 * assimilation_coef * multiplier * vector
    colonies = np.clip(colonies, lower_bound, upper_bound)

    empire[1:len(empire)] = colonies
    return empire
