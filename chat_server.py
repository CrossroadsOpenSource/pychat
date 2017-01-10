import socket
import constants


def startserver(IP=None):
    if IP is None:
        IP = 'localhost'
    # Create the socket and bind to the port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', constants.PORT)

    # Set the listen port
    sock.bind(server_address)
    sock.listen(1)
    # Connect
    while True:
        print("Waiting for connection on:{0}".format(server_address))
        connection, client_address = sock.accept()

        # TODO - Handle communication with this client
