**** VIEW IN RAW ****

# Port-Scanners
python scripts which are able to find the open ports on the target IP :)

**** VIEW IN RAW ****

Usage:

#1. Port.py
  Takes host IP and number of ports to be scanned as input. Tells whether the port is open or closed.
  
  root@kali:~# python3 Port.py
  
[*] Enter the IP Address: 8.8.8.8
[*] Number of Ports to Scan: 80
[-] 1/tcp is Closed
[-] 2/tcp is Closed
[-] 3/tcp is Closed
[-] 4/tcp is Closed
[-] 5/tcp is Closed
[-] 6/tcp is Closed
[-] 7/tcp is Closed
[-] 8/tcp is Closed
        .
        .
        .
[+] 80/tcp is Open


---------------------------------------------------------------------------------------------------------------------------------


#2. Advscan.py
  It's a better version of previous one, can specify the exact ports to be scanned and can take input from the command line.
  
  root@kali:~# python3 Advscan.py -H www.google.com -p 80,20,21,22,23,24,25
  
[+] Scan results for: kix05s07-in-f4.1e100.net
[+] 80/tcp is Open
[-] 21/tcp is Closed
[-] 20/tcp is Closed
[-] 23/tcp is Closed
[-] 22/tcp is Closed
[-] 25/tcp is Closed
[-] 24/tcp is Closed
