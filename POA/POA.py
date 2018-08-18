# Parliamentary Political Competitions: A New Approach To Global Optimization
# As seen in the paper by Ali Borji & Mandana Hamidi
# Implemented by Juanjo Sierra

from DefineInitialParties import *
from IntraGroupCompetition import *
from InterGroupCooperation import *

def POA(CostFunction, dim=10, nparties=4, nmembers=5, ncandidates=2,
		lower_bound=0, upper_bound=10, max_eval=10000, merge_probability=0.01,
		deletion_probability=0.001, bias=0.3, member_weighting=0.01,
		candidate_weighting=1, groups_to_merge=2, groups_to_delete=1):

	# Domain of the function, tuple including lower and upper bounds
	domain = (lower_bound, upper_bound)

	# Define the initial parties and candidates
	candidates, candidates_fitness, members, members_fitness = DefineInitialParties(CostFunction,
			nparties, nmembers, ncandidates, dim, domain)

	evaluations = nparties * nmembers
	group_power = np.zeros(nparties)

	while evaluations < max_eval:
		for i in range(0,len(candidates)):
			# Intragroup Competition: regular members try to become candidates of their group
			candidates[i], candidates_fitness[i], members[i], members_fitness[i], group_power[i], new_evaluations = IntraGroupCompetition(CostFunction,
					candidates[i], candidates_fitness[i], members[i], members_fitness[i], domain,
					bias, candidate_weighting, member_weighting)

		# Intergroup Cooperation: best groups try to merge into a greater one, and weakest groups may disappear
		candidates, candidates_fitness, members, members_fitness, group_power = InterGroupCooperation(candidates, candidates_fitness,
				members, members_fitness, group_power, groups_to_merge, merge_probability, groups_to_delete, deletion_probability)

		# print("Iteration {:4}, best solution: {:e}".format(iterations, np.min(candidates_fitness)))

		evaluations += new_evaluations
