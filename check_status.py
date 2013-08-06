#!/usr/bin/env python

import json, yaml, argparse, httpd, status


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check status script')
    parser.add_argument('--json', const='json', default='print', dest='output_format', action='store_const', help='return the status as json')
    parser.add_argument('--www', const=True, default=False, dest='start_httpd', action='store_const', help='return the status as json')
    args = parser.parse_args()

    if args.start_httpd:
        print 'Starting webserver...'
        httpd.LocalStatusHttpd() 
    else:
        if args.output_format == 'json':
            print status.getServicesStatus() 
        else:
            data = json.loads(status.getServicesStatus(services)) 
            for svc in data:
                print "{} ({}): {}".format(svc['service'], svc['port'], status.printStatus(svc['status']))
