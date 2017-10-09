import numpy as np

def CreateInitialLeague(settings):
    nteams = settings['nteams']
    nmain = settings['nmain']
    nres = settings['nres']
    dim = settings['dim']
    lower_bound = settings['lower_bound']
    upper_bound = settings['upper_bound']

    # We reshape to 2 for making a difference between main and reserve players of the same team.
    # The league has the following format: it is splitted into teams, which are as well splitted
    # into main and reserve players.
    league = np.random.uniform(lower_bound,upper_bound,nteams*2*nmain*dim).reshape(nteams,2,nmain,dim)

    # Now the 'Takhsis' is called for having the players sorted according to their fitness.
