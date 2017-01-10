import socket
import constants


def startclient(IP=None):
    if IP is None:
        IP = 'localhost'
    # Create the socket and bind to the port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (IP,constants.PORT)

    print("Attempting to connect to: {0}".format(server_address))
    # Try to connect
    sock.connect(server_address)

