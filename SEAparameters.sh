#!/bin/bash
#
# The name of the job, can be whatever makes sense to you
#SBATCH -J param-est-SEA

# The job should be placed into the queue 'larga'.
#SBATCH -p larga

# Redirect output stream to this file.
#SBATCH -o param-est-SEA.dat

# Redirect error stream to this file.
#SBATCH -e param-est-SEA-err.dat

#_______________________________________________________________________________

# SEA Parameter Estimation
python3 SEA/SEAparameters.py
