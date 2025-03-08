#!/bin/bash
#SBATCH --account=PAS2836
#SBATCH --job-name=check_multi_node_gpu
#SBATCH --time=00:01:00
#SBATCH --cluster=cardinal
#SBATCH --nodes=2
#SBATCH --gpus-per-node=1
#SBATCH --ntasks-per-node=1
#SBATCH --output=./%x_%j_%u.out

echo `date`

printf "from Bash\n"
for node in $(scontrol show hostnames $SLURM_JOB_NODELIST); do
    echo "Node: $node"
    ssh $node "nvidia-smi"
done

printf "\n\nfrom Python\n"
source ~/miniconda3/bin/activate dedup
python check_multi_node_gpus.py