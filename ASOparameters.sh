#!/bin/bash
#
# The name of the job, can be whatever makes sense to you
#SBATCH -J ASO-param

# The job should be placed into the queue 'larga'.
#SBATCH -p larga

# Redirect output stream to this file.
#SBATCH -o ASO-param.dat

# Redirect error stream to this file.
#SBATCH -e ASO-param-err.dat

#_______________________________________________________________________________

# ASO Parameter Estimation
python3 ASO/ASOparameters.py
