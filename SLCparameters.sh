#!/bin/bash
#
# The name of the job, can be whatever makes sense to you
#SBATCH -J param-est-SLC

# The job should be placed into the queue 'larga'.
#SBATCH -p larga

# Redirect output stream to this file.
#SBATCH -o param-est-SLC.dat

# Redirect error stream to this file.
#SBATCH -e param-est-SLC-err.dat

#_______________________________________________________________________________

# SLC Parameter Estimation
python3 SLC/SLCparameters.py
