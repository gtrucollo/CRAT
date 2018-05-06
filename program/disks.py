import psutil

def info():
    return psutil.disk_partitions()
