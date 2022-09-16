import psutil
from datetime import datetime
import json

def get_processes_info():
    processes, config = [], []
    for process in psutil.process_iter():
        with process.oneshot():
            pid = process.pid
            if pid == 0:
                continue
            name = process.name()
            try:
                create_time = datetime.fromtimestamp(process.create_time())
            except OSError:
                create_time = datetime.fromtimestamp(psutil.boot_time())
            try:
                cores = len(process.cpu_affinity())
            except psutil.AccessDenied:
                cores = 0
            cpu_usage = process.cpu_percent()
            status = process.status()
            try:
                memory_usage = process.memory_full_info().uss
            except psutil.AccessDenied:
                memory_usage = 0
            io_counters = process.io_counters()
            read_bytes = io_counters.read_bytes
            write_bytes = io_counters.write_bytes
            threads = process.num_threads()

        config.append({
            'name': name,
        })
        processes.append({
            'pid': pid,
            'name': name,
            'cores': cores,
            'cpu_usage': f'{str(cpu_usage)}%',
            'status': status,
            'memory_usage': get_size(memory_usage),
            'read_bytes': get_size(read_bytes),
            'write_bytes': get_size(write_bytes),
            'threads': threads,
        })

    with open("local_config.json", "w") as jsonize:
        json.dump(config, jsonize)

    return processes

def get_size(bytes):
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024