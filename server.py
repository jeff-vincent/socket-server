import socket

class SocketServer:

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.HEADERSIZE = 10

    def main(self):
        self.s.bind((socket.gethostname(), 8081))
        self.s.listen(5)

        while True:
            clientsocket, address = self.s.accept()
            print('A connection to {} has been made!'.format(address))
            msg = 'Welcome to the server!'
            
            msg_with_header = f'{len(msg):<{self.HEADERSIZE}}' + msg
            
            clientsocket.send(bytes(msg_with_header, 'utf-8'))


if __name__ == '__main__':
    server = SocketServer()
    server.main()