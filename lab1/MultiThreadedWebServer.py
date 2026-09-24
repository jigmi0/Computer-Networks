# Optional Exercise 1
# multithreaded web server
from socket import *
import threading
import sys

def handle_client(connectionSocket, addr):
    try:
        message = connectionSocket.recv(1024).decode()
        if not message:
            return
        filename = message.split()[1]
        with open(filename[1:]) as f:
            outputdata = f.read()
        connectionSocket.sendall("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode())
        connectionSocket.sendall(outputdata.encode())
        connectionSocket.sendall("\r\n".encode())
    except (IOError, IndexError):
        connectionSocket.sendall("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n".encode())
        connectionSocket.sendall("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
    finally:
        connectionSocket.close()

serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)

try:
    while True:
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        # Each request/response pair is handled on its own connection in its own thread
        t = threading.Thread(target=handle_client, args=(connectionSocket, addr), daemon=True)
        t.start()
except KeyboardInterrupt:
    pass
finally:
    serverSocket.close()
    sys.exit()
