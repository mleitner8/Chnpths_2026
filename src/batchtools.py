from netpyne.batchtools.search import search

params = {'seeds.conn': [4321 + (17 * i) for i in range(5)],
          'seeds.stim': [1234 + (17 * i) for i in range(5)],
          'seeds.loc': [4321 + (17 * i) for i in range(5)]
          }

sge_config = {
    'queue': 'cpu.q',
    'cores': 64,
    'vmem': '120G',
    'realtime': '15:00:00',
    'command': 'mpiexec -n $NSLOTS -hosts $(hostname) nrniv -python -mpi init_batch.py'}


run_config = sge_config

results = search(job_type = 'sge', # or 'sh'
       comm_type = 'socket', # if a metric and mode is specified, some method of communicating with the host needs to be defined
       label = 'seeds_1',
       params = params,
       output_path = '../batchData/seed_batch',
       checkpoint_path = '../batchData/ray',
       run_config = run_config,
       metric = 'loss', # if a metric and mode is specified, the search will collect metric data and report on the optimal configuration
       num_samples=1,
       mode = 'min',
       algorithm = 'grid',
       max_concurrent = 9 )
