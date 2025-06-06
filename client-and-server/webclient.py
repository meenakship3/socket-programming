import socket
import sys

"""
Client sends ISO-8858-1 encoded request to a webserver and prints decoded response. Host and port can be entered by user.
"""
host = sys.argv[1]
if len(sys.argv) > 2:
    port = int(sys.argv[2])
else:
    port = 80

client_socket = socket.socket()

try:
    client_socket.connect((host, port))
    http_request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

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
