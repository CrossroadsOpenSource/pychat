import sys
import socket
import chat_client
import chat_server
import asyncore

def servermain():
    # Get the IP address
    IP = get_local_hostname()
    print("Starting server...")
    print("Server IP:{0}".format(IP))

    chat_server.start_server(IP)


def get_local_hostname():
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    return IP


def clientmain():
    print("Chat client!")

    IP_addr = input("Server IP address [{0}]:".format(get_local_hostname()))

    if len(IP_addr) == 0:
        IP_addr = get_local_hostname()

    chat_client.start_client(IP_addr)


# Main entry point.
if __name__ == "__main__":
    # Determine if we are a client or a server
    if "-server" in sys.argv:
        servermain()
    elif "-client" in sys.argv:
        clientmain()
    elif "-test" in sys.argv:
        # Spawn the server and the client on separate threads
        servermain()
        clientmain()

        asyncore.loop()