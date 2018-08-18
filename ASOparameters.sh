#!/bin/bash
#
# The name of the job, can be whatever makes sense to you
#SBATCH -J param-est-ASO

# The job should be placed into the queue 'larga'.
#SBATCH -p larga

# Redirect output stream to this file.
#SBATCH -o param-est-ASO.dat

# Redirect error stream to this file.
#SBATCH -e param-est-ASO-err.dat

#_______________________________________________________________________________

# ASO Parameter Estimation
python3 ASO/ASOparameters.py
