from socket import *
from codecs import decode
client = socket(AF_INET,SOCK_STREAM)
host = "localhost"
port = 80
adr = (host,port)
client.connect(adr)
client.send(b'Hi I am client')
from_server = decode(client.recv(4096))
client.close()
print(from_server)