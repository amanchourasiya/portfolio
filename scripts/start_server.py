#!/usr/bin/env python3

'''
This script will setup the server environment including getting files from persistent storage
and start server after running some pre checks.

This will setup config based on development/production environment
'''

import sys
import os

def usage():
    print('Script usage')
    print('python3 start_server.py <server-mode>')
    print('server-mode: dev/prod')

def dev_mode():
    pass

def prod_mode():
    # Download images and blog JSON from persistent storage
    try:
        port = os.environ['PORT']
    except:
        port = 80
    os.system('gunicorn -b 0.0.0.0:' + str(port) + ' --chdir portfolio/ portfolio.wsgi --log-file -')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    else:
        mode = sys.argv[1]
        if mode == 'dev':
            dev_mode()
        elif mode == 'prod':
            prod_mode()
        else:
            usage()

