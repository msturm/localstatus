#!/usr/bin/env python
import socket, yaml, json, argparse, httpd, status

class color:
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    ENDC = '\033[0m'

    @staticmethod
    def red(content):
        return color.RED + content + color.ENDC

    @staticmethod
    def green(content):
        return color.GREEN + content + color.ENDC

def isPortOpen(port, host="localhost"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, int(port)))
        s.shutdown(2)
        return True
    except:
        return False

def serviceRunning(port, host):
    if isPortOpen(port, host):
        return "RUNNING"
    else:
        return "DOWN"

def checkServiceStatus(service):
    name = service['service']
    port = service['port']
    if 'host' in service:
        host = service['host']
    else:
        host = 'localhost'

    return {"service": name, "port": port, "status": serviceRunning(port, host)}
   
def getServicesStatus():
    f = open("services.yaml", 'r')
    text = f.read()
    f.close()
    services = yaml.load(text) 
    return json.dumps([checkServiceStatus(service) for service in services['services']]) 

def printStatus(status): 
    if status == "RUNNING":
        return color.green(status)
    else:
        return color.red(status) 
