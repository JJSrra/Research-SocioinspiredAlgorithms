#!/bin/bash
#
# The name of the job, can be whatever makes sense to you
#SBATCH -J ASO-30-1

# The job should be placed into the queue 'larga'.
#SBATCH -p larga

# Redirect output stream to this file.
#SBATCH -o ASO-exp-30-1.dat

# Redirect error stream to this file.
#SBATCH -e ASO-exp-30-1-err.dat

#_______________________________________________________________________________

# ASO Experiments
python3 ~/ASO/ASObenchmark30-1.py
