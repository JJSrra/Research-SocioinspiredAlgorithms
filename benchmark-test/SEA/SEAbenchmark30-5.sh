#!/bin/bash
#
# The name of the job, can be whatever makes sense to you
#SBATCH -J SEA-30-5

# The job should be placed into the queue 'larga'.
#SBATCH -p larga

# Redirect output stream to this file.
#SBATCH -o SEA-exp-30-5.dat

# Redirect error stream to this file.
#SBATCH -e SEA-exp-30-5-err.dat

#_______________________________________________________________________________

# SEA Experiments
python3 ~/SEA/SEAbenchmark30-5.py
