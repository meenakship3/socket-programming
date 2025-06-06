import socket
import sys

"""
Server that runs forever, listening for incoming requests. Sends back a simple response.
"""

if len(sys.argv) > 1:
    port = int(sys.argv[1])
else:
    port = 28333

print(f"Starting server on port {port}")

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(('',port))
server_socket.listen()

try:
    while True:
        new_conn = server_socket.accept()
        new_socket = new_conn[0]

        request = b''
        while True:
            data = new_socket.recv(1024)
            if not data:
                break
            request += data
            if b'\r\n\r\n' in request:
                break
        print(request.decode("ISO-8859-1"))

        response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 5\r\nConnection: close\r\n\r\nHello"

        new_socket.send(response.encode("ISO-8859-1"))
        new_socket.close()

except KeyboardInterrupt:
    print("Shutting down server...")

finally:
    server_socket.close()


