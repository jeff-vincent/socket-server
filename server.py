import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8081))

s.listen(5)

while True:
    clientsocket, address = s.accept()
    print('A connection to {} has been made!'.format(address))
    msg = 'Welcome to the server!'
    
    msg_with_header = f'{len(msg):<{HEADERSIZE}}' + msg
    
    clientsocket.send(bytes(msg_with_header, 'utf-8'))