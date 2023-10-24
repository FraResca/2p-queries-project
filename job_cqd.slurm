#!/bin/bash
#SBATCH --job-name=cqd_job
#SBATCH --nodes=1
#SBATCH --time=05:00:00
#SBATCH --error=cqd_job.err
#SBATCH --output=cqd_job.out
#SBATCH --partition=longrun
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=35G
#SBATCH --gres=gpu:4

 
module load conda
 
conda run 2p-queries-project python3 starter.py