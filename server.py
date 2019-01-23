import socket
import base64


HOST = '127.0.0.11'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

drivers_connections = []
passengers_connections = []

while True:
    conn, addr = s.accept()
    conn.sendall(b'start')
    if conn.recv(1024) == b'driver':
        conn.sendall(b'continue')
        score = base64.b64decode(conn.recv(1024))
        drivers_connections.append([score, conn])
        conn.sendall(b'end')
    else:
        conn.sendall(b'continue')

