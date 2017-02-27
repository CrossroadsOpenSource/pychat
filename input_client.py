import asyncore


class CmdlineClient(asyncore.file_dispatcher):
    def __init__(self, client, file):
        asyncore.file_dispatcher.__init__(self,file)
        self.client = client

    def handle_read(self):
        self.sender.buffer += self.recv(1024)