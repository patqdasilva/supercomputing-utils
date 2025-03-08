def print_multi_node_gpu() -> None:
    """Print nvidia-smi for every node in current SLURM job.
    
    from Patrick Q. Da Silva, inspired from:
        https://github.com/facebookresearch/fairseq/
        blob/main/fairseq/distributed/utils.py

    """
    import os
    import subprocess
    print('print_multi_node_gpu:\tstart.')
    nodes = os.getenv("SLURM_JOB_NODELIST")
    if nodes:
        node_list = subprocess.check_output(
            ["scontrol", "show", "hostnames", nodes]
        ).decode().split()
    else:
        node_list = []
    print(f'print_multi_node_gpu:\tlisting nodes found: {node_list}.')
    for node in node_list:
        print(f'Node: {node}')
        result = subprocess.run(
            ["ssh", node, "nvidia-smi"],
            capture_output=True, text=True
        )
        print(result.stdout)
    print('print_multi_node_gpu:\tcomplete.')
    return None

if __name__ == '__main__':
    print_multi_node_gpu()