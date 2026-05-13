#from batchtk.algos import optuna_search
from netpyne.batchtools.search import search, grid
#from batchtk.utils import expand_path
#from netpyne.batchtools.search import generate_constructors



params = {
          'seeds.conn': [4321 + (17 * i) for i in range(5)],
          'seeds.stim': [1234 + (17 * i) for i in range(5)]
          } 


search(job_type='suny',
       comm_type='sfs',
       params = params,
       run_config={
        'realtime': '120:00:00',
        'cores':64,
        'mem': '128G',
        'script': 'init_batch.py'},
        label='gridSearch_seeds',
        output_path='./grid_batch',
        checkpoint_path='./batch_checkpoints')