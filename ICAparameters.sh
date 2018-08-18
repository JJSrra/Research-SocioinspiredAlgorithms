#!/bin/bash
#
# The name of the job, can be whatever makes sense to you
#SBATCH -J param-est-ICA

# The job should be placed into the queue 'larga'.
#SBATCH -p larga

# Redirect output stream to this file.
#SBATCH -o param-est-ICA.dat

# Redirect error stream to this file.
#SBATCH -e param-est-ICA-err.dat

#_______________________________________________________________________________

# ICA Parameter Estimation
python3 ICA/ICAparameters.py
