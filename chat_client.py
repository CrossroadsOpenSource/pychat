import socket
import constants
import asyncore
import sys
import input_client


def start_client(IP):
    cc = ChatClient(IP, 4321)
    # Create cmd handler
    cmdclient = input_client.CmdlineClient(cc,sys.stdin)


class ChatClient(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))

        self.buffer = ''

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()

    def handle_read(self):
        print(self.recv(8192))

    def writable(self):
        return len(self.buffer) > 0

    def handle_write(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]

    def write_data(self, data):
        self.buffer += data