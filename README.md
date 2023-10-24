# 2-hop-queries: time based comparison between gradiend based and logic programming approaches - Francesco Resca

Download dataset and pretrained models by launching this script
```bash
./dataandmodel.sh
```

Prepare the conda environment for the gradient based method
```bash
conda create --name 2p-queries-project python=3.8 && conda activate 2p-queries-project
pip install -r requirements.txt
```

Create the facts and the queries prolog files
```bash
./factandqueries.sh
```

Verify the correctness of the queries
```bash
swipl verify.pl
```
Correct results look like this:
```bash
Total:8000
Correct:8000
```

Submit the jobs to the COKA cluster
```bash
sbatch job_cqd.slurm
sbatch job_qpl.slurm
```