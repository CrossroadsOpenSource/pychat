import socket
import constants
import asyncore


def start_server(IP):
    cs = ChatServer(IP,4321)


class ClientHandler(asyncore.dispatcher_with_send):

    def __init__(self, sock, server):
        asyncore.dispatcher_with_send.__init__(self, sock=sock)

        # Add myself to the master list
        server.active_clients.append(self)
        self.server = server

    def handle_read(self):
        data = self.recv(8192)
        if data:
            print("data=", data)

    def write_data(self, data):
        self.send(data)

    def handle_close(self):
        # Remove myself from the master list
        self.server.remove(self)



class ChatServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host,port))
        self.listen(5)

        # Master list of clients
        self.active_clients = []

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print('Incoming connection from ',repr(addr))
            handler = ClientHandler(sock, self)

    def post_data(self, client, data):
        # Send this data out to the clients
        recv_clients = [cl for cl in self.active_clients if cl is not client]

        for cl in recv_clients:
            cl.write_data(data)

