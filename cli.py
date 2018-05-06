from program import computer, cpu, memory, tools, disks, network
import sys

params = sys.argv

if  len(params) > 1:
	if params[1] == "os" or params[1] == "system":
		print("Sistema Operacional: ",computer.os() , computer.osVersion())
	elif params[1] == "name":
		print("Nome de rede:", computer.name())
	elif params[1] == "distro":
		print("Distribuicao:", computer.distro())
	elif params[1] == "processor" or params[1] == "-p":
		if len(params) == 4  and params[2] == "percentage" and  int(params[3]) >= 1:
			for x in range(int(params[3])):
				consumo = cpu.cpu_percent()
				print("Comsumo",consumo.user + consumo.system , "%")
				print("Livre: ",consumo.idle, "%")
		elif len(params) == 4  and params[2] == "bench" and  int(params[3]) >= 1:
			media = 0
			for x in range(int(params[3])):
				consumo = cpu.cpu_percent()
				media += consumo.user + consumo.system
			media = media/int(params[3])
			print("Consumo médio: ",media, "%")
		else:	
			print("Processador: ", computer.cpu())
			print("Clock: ", cpu.freq(), "Ghz")
			print("Cores: ", cpu.cores())
			print("Cores fisicos: ", cpu.coresF())
	elif params[1] == "memory" or params[1] == "-m":
		if str(params).find("size") > 0:
			print("Memoria ram instalada: ", memory.size(), "GB")
		if str(params).find("percentage") > 0:
			print("Consumo Atual da Memoria", memory.percentage(),"%")
		if str(params).find("free") > 0:
			print("Memoria ram livre :", memory.free(), "GB")
		if str(params).find("used") > 0:
			print("Memoria usada", memory.used(), "GB")	
	elif params[1] == "disks" or params[1] == "-d" :
		if str(params).find("info") > 0:
			diskList = disks.info()
			i = 0
			while i < len(diskList):
				print("Ponto de Montagem", diskList[i].mountpoint)
				print("Sistema de Arquivos", diskList[i].fstype)
	elif params[1] == "network" or params[1] == "-n":
		if(str(params).find("bytes")) >0:
			bytesN = network.info()
			print("Bytes enviados: ", bytesN.bytes_sent/(1024 * 1024 * 1024))
			print("Bytes recebidos: ", bytesN.bytes_recv/(1024 * 1024 * 1024))		
	elif params[1] == "arch":
		print("Arquitetura do computador: ", computer.arch())
	elif str(params).find("shutdown") > 0:
		print("Sistema será desligado em seguida")
		tools.shutdown()
	elif str(params).find("reboot") > 0:
		print("Sistema será reiniciado em seguida")
		tools.reboot()	
	else:
		print("Parametro desconhecido")	
else:
	print("Você não passou nenhum parametro")