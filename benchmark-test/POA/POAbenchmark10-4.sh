#!/bin/bash
#
# The name of the job, can be whatever makes sense to you
#SBATCH -J POA-10-4

# The job should be placed into the queue 'larga'.
#SBATCH -p larga

# Redirect output stream to this file.
#SBATCH -o POA-exp-10-4.dat

# Redirect error stream to this file.
#SBATCH -e POA-exp-10-4-err.dat

#_______________________________________________________________________________

# POA Experiments
python3 ~/POA/POAbenchmark10-4.py
