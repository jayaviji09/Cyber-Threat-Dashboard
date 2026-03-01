import psutil
import time

def monitor_system():
    """Captures system metrics over a short interval."""
    
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    used_mem_gb = round(memory.used / (1024**3), 2)
    return cpu_usage, used_mem_gb