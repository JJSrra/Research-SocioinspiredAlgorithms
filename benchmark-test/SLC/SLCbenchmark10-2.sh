#!/bin/bash
#
# The name of the job, can be whatever makes sense to you
#SBATCH -J SLC-10-2

# The job should be placed into the queue 'larga'.
#SBATCH -p larga

# Redirect output stream to this file.
#SBATCH -o SLC-exp-10-2.dat

# Redirect error stream to this file.
#SBATCH -e SLC-exp-10-2-err.dat

#_______________________________________________________________________________

# SLC Experiments
python3 ~/SLC/SLCbenchmark10-2.py
