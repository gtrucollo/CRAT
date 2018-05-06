import psutil

def freq():
	return round(psutil.cpu_freq().current/1000.0000,1)
def cores():
	return psutil.cpu_count()
def coresF():
	return psutil.cpu_count(logical=False)
def cpu_percent():
	return psutil.cpu_times_percent(interval=1)