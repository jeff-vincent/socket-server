import socket

class SocketClient:

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.HEADERSIZE = 10

    def main(self):
        self.s.connect((socket.gethostname(), 8081))

        while True:
            full_msg = ''
            new_msg = True

            while True:
                msg = self.s.recv(16)
                if new_msg:
                    msg_length = int(msg[:self.HEADERSIZE])
                    new_msg = False

                full_msg += msg.decode('utf-8')

                if len(full_msg) - self.HEADERSIZE == msg_length:
                    print('Full message recieved: {}'.format(full_msg[self.HEADERSIZE:]))
                    full_msg = ''

if __name__ == '__main__':
    client = SocketClient()
    client.main()