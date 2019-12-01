#!/usr/bin/python3

import socket
from termcolor import colored


host = str(input(colored("[*] Enter the IP Address: ", 'blue')))
r = int(input(colored("[*] Number of Ports to Scan: ", 'blue')))
# Remove the comment to scan a specific port
# p = int(input("[*] Enter the Port to Scan: "))


def port_scanner(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(10)
        sock.settimeout(10)

        sock.connect((host, port))
        print(colored('[+] %d/tcp is Open ' % port, 'green'))
    except:
        print(colored('[-] %d/tcp is Closed' % port, 'red'))


for p in range(1, r+1):
    port_scanner(p)
