# 2-hop-queries: time based comparison between gradient based and logic programming approaches - Francesco Resca

Download dataset and pretrained models by launching this script:
```bash
./dataandmodel.sh
```

Prepare the conda environment for the gradient based method:
```bash
conda create --name cqd python=3.8 && conda activate cqd
pip install -r requirements.txt
```

Create the files for prolog facts and queries:
```bash
./factandqueries.sh
```

Verify the correctness of the queries:
```bash
swipl verify.pl
```
Correct results look like this:
```bash
Total:8000
Correct:8000
```

Submit the jobs to the COKA cluster:
```bash
sbatch job_cqd.slurm
sbatch job_qpl.slurm
```

The cqd job executes experiments on four different neural predictors having rank 100, 200, 500 and 1000. When the execution terminates there should be four json files named topk_d=FB15k_t=product_e=1_2_rank=*_k=64_sn=0.json with metrics and answering times from each experiment.

The qpl job is able to execute only one experiment for each execution, to obtain multiple measurements it is necessary to submit the job more than once. The measurement is stored on the qpl_job.err file and not on the qpl_job.out file for unknown reasons.