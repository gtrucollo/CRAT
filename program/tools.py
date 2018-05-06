import os
from . import computer

def shutdown():
    if computer.os() =="Windows":
        os.system("shutdown -s")
    elif computer.os() == "Linux":
        os.system("shutdown -h")
    else:        
        print("Sistema operacional não suportado")
def reboot():
    if computer.os() == "Windows":
        os.system("shutdown -r")
    elif computer.os() == "Linux":
        os.system("restart")
    else:
        print("Sistema operacional não suportado")        
      