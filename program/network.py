import psutil

def info():
	return psutil.net_io_counters(pernic=False)