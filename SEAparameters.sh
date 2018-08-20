#!/bin/bash
#
# The name of the job, can be whatever makes sense to you
#SBATCH -J SEA-param

# The job should be placed into the queue 'larga'.
#SBATCH -p larga

# Redirect output stream to this file.
#SBATCH -o SEA-param.dat

# Redirect error stream to this file.
#SBATCH -e SEA-param-err.dat

#_______________________________________________________________________________

# SEA Parameter Estimation
python3 SEA/SEAparameters.py
