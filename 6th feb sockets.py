"""from socket import *
from codecs import decode
serv = socket(AF_INET,SOCK_DGRAM)
serv.bind(("10.228.7.57", 80))

while True:
    print("Waiting+")
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += decode(data)
        print (from_client)
        conn.send(b"I am SERVER\n")

    conn.close()
    print('client disconnected')"""

from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM,gethostname
import sys
PORT_NUMBER = 5000
SIZE = 1024

hostName = gethostbyname(gethostname())
print(hostName)

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

print ("Test server listening on port {0}\n".format(PORT_NUMBER))

while True:
        (data,addr) = mySocket.recvfrom(SIZE)
        print (data)
sys.ext()