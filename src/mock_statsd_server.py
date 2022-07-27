import socket
import os

server = os.getenv('STATSD_SERVER', default="localhost")
port = os.getenv('STATSD_PORT', default=8125)

#sock = socket.socket(socket.AF_INET, # Internet
#                 socket.SOCK_DGRAM) # UDP
sock = socket.socket() # TCP
sock.bind((server, port))
sock.listen(5)

while True:
    (clientSocket, clientAddress) = sock.accept()
    while True:
        data = clientSocket.recv(1024) # buffer size is 1024 bytes
        if len(data) == 0:
            break
        print("received message: ", data.strip())

