import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8080))

s.listen(5)

while True:
    clientsocket, address = s.accept()
    print('A connection to {} has been made!'.format(address))
    clientsocket.send(bytearray('Welcome to the server!', 'utf-8'))
    clientsocket.close()