import socket
import base64


class driver_client:
    HOST = '127.0.0.11'
    PORT = 65432

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.HOST, self.PORT))

    def wait(self):
        self.s.recv(1024)

    def declare(self):
        self.s.sendall(b'driver')

    def send_info(self,  score):
        self.s.sendall(base64.b64encode(score))

