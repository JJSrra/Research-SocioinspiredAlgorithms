#!/bin/bash
#
# The name of the job, can be whatever makes sense to you
#SBATCH -J POA-param

# The job should be placed into the queue 'larga'.
#SBATCH -p larga

# Redirect output stream to this file.
#SBATCH -o POA-param.dat

# Redirect error stream to this file.
#SBATCH -e POA-param-err.dat

#_______________________________________________________________________________

# POA Parameter Estimation
python3 POA/POAparameters.py
