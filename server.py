import socket
import random

class SocketServer:

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.HEADERSIZE = 10
        self.msg = ''

    def generate_msg(self):
        self.msg = str(random.random())

    def main(self):
        self.s.bind((socket.gethostname(), 8085))
        self.s.listen(5)

        while True:
            clientsocket, address = self.s.accept()
            print('A connection to {} has been made!'.format(address))
            

            self.generate_msg()
            msg_with_header = f'{len(self.msg):<{self.HEADERSIZE}}' + self.msg
    
            clientsocket.send(bytes(msg_with_header, 'utf-8'))



if __name__ == '__main__':
    server = SocketServer()
    server.main()