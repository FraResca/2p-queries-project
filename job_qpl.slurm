#!/bin/bash
#SBATCH --job-name=qpl_job
#SBATCH --nodes=1
#SBATCH --time=00:30:00
#SBATCH --error=qpl_job.err
#SBATCH --output=qpl_job.out
#SBATCH --partition=shortrun
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=35G
#SBATCH --gres=gpu:4

srun /home/dazzolin/swipl-devel/build/src/./swipl job_queries.pl
