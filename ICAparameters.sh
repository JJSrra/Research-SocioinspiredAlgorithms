#!/bin/bash
#
# The name of the job, can be whatever makes sense to you
#SBATCH -J ICA-param

# The job should be placed into the queue 'larga'.
#SBATCH -p larga

# Redirect output stream to this file.
#SBATCH -o ICA-param.dat

# Redirect error stream to this file.
#SBATCH -e ICA-param-err.dat

#_______________________________________________________________________________

# ICA Parameter Estimation
python3 ICA/ICAparameters.py
