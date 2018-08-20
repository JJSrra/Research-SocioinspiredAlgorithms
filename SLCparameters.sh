#!/bin/bash
#
# The name of the job, can be whatever makes sense to you
#SBATCH -J SLC-param

# The job should be placed into the queue 'larga'.
#SBATCH -p larga

# Redirect output stream to this file.
#SBATCH -o SLC-param.dat

# Redirect error stream to this file.
#SBATCH -e SLC-param-err.dat

#_______________________________________________________________________________

# SLC Parameter Estimation
python3 SLC/SLCparameters.py
