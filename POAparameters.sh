#!/bin/bash
#
# The name of the job, can be whatever makes sense to you
#SBATCH -J param-est-POA

# The job should be placed into the queue 'larga'.
#SBATCH -p larga

# Redirect output stream to this file.
#SBATCH -o param-est-POA.dat

# Redirect error stream to this file.
#SBATCH -e param-est-POA-err.dat

#_______________________________________________________________________________

# POA Parameter Estimation
python3 POA/POAparameters.py
