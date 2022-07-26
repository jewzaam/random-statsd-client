import socket
import os

server = os.getenv('STATSD_SERVER', default="localhost")
port = os.getenv('STATSD_PORT', default=8125)

sock = socket.socket(socket.AF_INET, # Internet
                 socket.SOCK_DGRAM) # UDP
sock.bind((server, port))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: ", data.strip())
