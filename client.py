import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 8081))

HEADERSIZE = 10

while True:
    full_msg = ''
    new_msg = True

    while True:
        msg = s.recv(16)
        if new_msg:
            msg_length = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg.decode('utf-8')

        if len(full_msg) - HEADERSIZE == msg_length:
            print('Full message recieved: {}'.format(full_msg[HEADERSIZE:]))
            full_msg = ''

