import socket
import time

"""Connects to the atomic clock at National Institute of Standards and Technology and gets the number of seconds 
since January 1, 1900. Also prints system time from the computer."""
def system_seconds_since_1900():
    """ The time server returns the number of seconds since 1900, but Unix systems return the number of seconds since
    1970. This function computes the number of seconds since 1900 on the system."""
    # Number of seconds between 1900-01-01 and 1970-01-01
    seconds_delta = 2208988800
    seconds_since_unix_epoch = int(time.time())
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta
    return seconds_since_1900_epoch


HOST = "time.nist.gov"
PORT = 37
client_socket = socket.socket()

try:
    client_socket.connect((HOST, PORT))

    time_data = client_socket.recv(4)
    client_socket.close()

    if len(time_data) == 4:
        nist_time = int.from_bytes(time_data, "big")
        print(f"NIST time: {nist_time}")
        system_time = system_seconds_since_1900()
        print(f"System time: {system_time}")
        print(f"Difference: {abs(nist_time - system_time)} seconds")
    else:
        print(f"Expected 4 bytes, received {len(time_data)} instead")

except socket.error as e:
    print(f"Error connecting: {e}")
    exit()

