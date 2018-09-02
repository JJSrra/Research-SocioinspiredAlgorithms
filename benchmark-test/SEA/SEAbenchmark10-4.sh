#!/bin/bash
#
# The name of the job, can be whatever makes sense to you
#SBATCH -J SEA-10-4

# The job should be placed into the queue 'larga'.
#SBATCH -p larga

# Redirect output stream to this file.
#SBATCH -o SEA-exp-10-4.dat

# Redirect error stream to this file.
#SBATCH -e SEA-exp-10-4-err.dat

#_______________________________________________________________________________

# SEA Experiments
python3 ~/SEA/SEAbenchmark10-4.py
