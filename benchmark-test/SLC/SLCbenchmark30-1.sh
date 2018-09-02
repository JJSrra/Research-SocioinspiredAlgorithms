#!/bin/bash
#
# The name of the job, can be whatever makes sense to you
#SBATCH -J SLC-30-1

# The job should be placed into the queue 'larga'.
#SBATCH -p larga

# Redirect output stream to this file.
#SBATCH -o SLC-exp-30-1.dat

# Redirect error stream to this file.
#SBATCH -e SLC-exp-30-1-err.dat

#_______________________________________________________________________________

# SLC Experiments
python3 ~/SLC/SLCbenchmark30-1.py
