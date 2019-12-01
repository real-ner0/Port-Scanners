#!/usr/bin/python

import optparse
from socket import *
from threading import *


def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print("[+] %d/tcp is Open" % tgtPort)
    except:
        print("[-] %d/tcp is Closed" % tgtPort)
    finally:
        sock.close()


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("Failed to resolve host :(")

    try:
        tgtName = gethostbyaddr(tgtHost)
        print("[+] Scan results for: " + tgtName[0])
    except:
        print("[+] Scan results for: " + tgtHost)
    setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()


def main():
    parser = optparse.OptionParser("Usage of Program: " + "-H <Target IP>   -p <Ports>")
    parser.add_option("-H", dest='tgtHost', type='string', help='Please specify the host...!')
    parser.add_option("-p", dest='tgtPort', type='string', help='Please specify ports, separated by commas...!')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = str(options.tgtPort).split(',')

    if (tgtHost is None) or (tgtPort is None):
        print(parser.usage)
        exit(0)

    portScan(tgtHost, tgtPort)


main()
