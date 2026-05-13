#!/bin/bash
#SBATCH --job-name=M1_UCDavis_12HH16HH_74aee313_NEWCELL_SEEDS_Batch
#SBATCH --output=/ddn/mleitner8/Chnpths_2026/src/batch_results/UCDavis_1216_74aee313_NEWPT5B_SEEDS_3.log.run
#SBATCH --error=/ddn/mleitner8/Chnpths_2026/src/batch_results/UCDavis_1216_74aee313_NEWPT5B_SEEDS_3.log.err

source ~/.bashrc
conda activate M1c_batch
cd /ddn/mleitner8/Chnpths_2026/src

python batchtools_slurm.py