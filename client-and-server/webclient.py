import socket
import sys

host = sys.argv[1]
port = 80 or sys.argv[2]
client_socket = socket.socket()
try:
    client_socket.connect((host, port))
except socket.error as e:
    print(f"Error connecting: {e}")
    exit()

http_request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\n"

client_socket.sendall(http_request.encode("ISO-8859-1"))

response = b''
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    response += data

response_decoded = response.decode("ISO-8859-1")

print(response_decoded)

client_socket.close()
