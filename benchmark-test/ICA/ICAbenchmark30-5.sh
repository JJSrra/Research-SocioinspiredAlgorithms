#!/bin/bash
#
# The name of the job, can be whatever makes sense to you
#SBATCH -J ICA-30-5

# The job should be placed into the queue 'larga'.
#SBATCH -p larga

# Redirect output stream to this file.
#SBATCH -o ICA-exp-30-5.dat

# Redirect error stream to this file.
#SBATCH -e ICA-exp-30-5-err.dat

#_______________________________________________________________________________

# ICA Experiments
python3 ~/ICA/ICAbenchmark30-5.py
