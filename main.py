import sys
import socket
import chat_client
import chat_server
import threading

def servermain():
    # Get the IP address
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    print("Starting server...")
    print("Server IP:{0}".format(IP))

    chat_server.startserver(IP)


def clientmain():
    print("Chat client!")

    IP_addr = input("Server IP address:")

    chat_client.startclient(IP_addr)


# Main entry point.
if __name__ == "__main__":
    # Determine if we are a client or a server
    if "-server" in sys.argv:
        servermain()
    elif "-client" in sys.argv:
        clientmain()
    elif "-test" in sys.argv:
        # Spawn the server and the client on separate threads
        client_thread = threading.Thread(target=clientmain)
        server_thread = threading.Thread(target=servermain)

        server_thread.daemon = True
        client_thread.daemon = False

        server_thread.start()
        client_thread.start()