#!/usr/bin/env python

import socket, yaml, json, argparse


def isPortOpen(port, host="localhost"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, int(port)))
        s.shutdown(2)
        return True
    except:
        return False

def serviceRunning(port):
    if isPortOpen(port):
        return "RUNNING"
    else:
        return "DOWN"

def checkServiceStatus(service):
    (name, port) = service.split(':')
    return {"service": name, "port": port, "status": serviceRunning(port)}
   
def getServicesStatus(services):
    return json.dumps([checkServiceStatus(service) for service in services['services']]) 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check status script')
    parser.add_argument('--json', const=json, default='print', dest='output_format', action='store_const', help='return the status as json')
    args = parser.parse_args()

    f = open("services.yaml", 'r')
    text = f.read()
    f.close()
    services = yaml.load(text) 
    if args.output_format == json:
        print getServicesStatus(services) 
    else:
        data = json.loads(getServicesStatus(services)) 
        for svc in data:
            print "{} ({}): {}".format(svc['service'], svc['port'], svc['status'])
