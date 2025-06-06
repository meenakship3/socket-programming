import os.path
import socket

"""
Server that runs forever, listening for incoming requests. Sends back a text/html file.
"""


def construct_response(decoded_request):
    # parse header and get file name
    request_details = decoded_request.split("\r\n")
    request_line = request_details[0]
    parts = request_line.split()
    if len(parts) >= 2:
        fullpath = parts[1]
    else:
        fullpath = "/"
    file_name = fullpath.lstrip("/")
    file_type = os.path.splitext(file_name)

    # get mime type
    mime_type = "text/plain" # default
    if file_type[1] == '.txt':
        mime_type = "text/plain"
    elif file_type[1] == ".html":
        mime_type = "text/html"

    # read file if it exists
    try:
        with open(file_name, "rb") as fp:
            data = fp.read()
            content_length = len(data)
            response_header = f"HTTP/1.1 200 OK\r\nContent-Type: {mime_type}\r\nContent-Length: {content_length}\r\nConnection: close\r\n\r\n"
            encoded_response = response_header.encode("ISO-8859-1") + data
    except FileNotFoundError:
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\nContent-Length: 13\r\nConnection: close\r\n\r\n404 not found"
        encoded_response = response.encode("ISO-8859-1")
    finally:
        return encoded_response


PORT = 33490

print(f"Starting server on port {PORT}")

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(('', PORT))
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

        decoded_request = request.decode("ISO-8859-1")
        response = construct_response(decoded_request)

        new_socket.send(response)
        new_socket.close()

except KeyboardInterrupt:
    print("Shutting down server...")

finally:
    server_socket.close()





