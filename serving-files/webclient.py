import socket
import sys

"""
Client requests a file from the webserver. 
"""
HOST = "localhost"
PORT = 33490
file_name = sys.argv[1]

client_socket = socket.socket()

try:
    client_socket.connect((HOST, PORT))
    http_request = f"GET {file_name} HTTP/1.1\r\nHost: {HOST}\r\nConnection: close\r\n\r\n"

    client_socket.sendall(http_request.encode("ISO-8859-1"))

    response = b''
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        response += data

    response_decoded = response.decode("ISO-8859-1")
    print(response_decoded)
except socket.error as e:
    print(f"Error connecting: {e}")
    exit()
except KeyboardInterrupt:
    print("\nConnection interrupted. Closing client...")
finally:
    client_socket.close()
