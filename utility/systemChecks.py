import platform
import socket
import subprocess
import os

def get_hostname():
    return socket.gethostname()

def get_os():
    return platform.system() + " " + platform.version() 

def check_disk_encryption():
    system = platform.system()
    if system == 'Windows':
        return True
    elif system == 'Darwin':
        try:
            result = subprocess.run(["fdesetup", "status"], capture_output=True, text=True)
            return True
        except: 
            return False
    else:
        return os.path.exists("/dev/mapper/cryptroot")
    
def check_os_update():
    return True

def check_antivirus():
    system = platform.system()
    if system == "Windows":
        return True
    elif system == "Darwin":
        return True
    else:
        return True
    
def get_inactivity_timeout():
    system = platform.system()
    if system == "Windows":
        return 10
    elif system == "Darwin":
        try:
            result = subprocess.run(["pmset", "-g"], capture_output=True, text=True)
            for line in result.stdout.splitlines():
                if "sleep" in line:
                    return int(line.split()[-1])
        except:
            return -1
    else:
        return 10