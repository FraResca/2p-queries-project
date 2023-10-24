#!/bin/bash
#SBATCH --job-name=cqd_job
#SBATCH --error=cqd_job.err
#SBATCH --output=cqd_job.out
#SBATCH --ntasks=4
#SBATCH --ntasks-per-node=4
 
module load conda
 
conda run 2p-queries-project python3 starter.py