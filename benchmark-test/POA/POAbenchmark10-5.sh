#!/bin/bash
#
# The name of the job, can be whatever makes sense to you
#SBATCH -J POA-10-5

# The job should be placed into the queue 'larga'.
#SBATCH -p larga

# Redirect output stream to this file.
#SBATCH -o POA-exp-10-5.dat

# Redirect error stream to this file.
#SBATCH -e POA-exp-10-5-err.dat

#_______________________________________________________________________________

# POA Experiments
python3 ~/POA/POAbenchmark10-5.py
