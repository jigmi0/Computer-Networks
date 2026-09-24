# Optional Exercise 2
# Usage: python client.py server_host server_port filename
from socket import *
import sys

if len(sys.argv) != 4:
    print("Usage: python client.py server_host server_port filename")
    sys.exit(1)

host, port, filename = sys.argv[1], int(sys.argv[2]), sys.argv[3]
if not filename.startswith('/'):
    filename = '/' + filename

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((host, port))
request = "GET {} HTTP/1.1\r\nHost: {}:{}\r\nConnection: close\r\n\r\n".format(filename, host, port)
clientSocket.send(request.encode())

response = b""
while True:
    data = clientSocket.recv(4096)
    if not data:
        break
    response += data
clientSocket.close()
print(response.decode())
