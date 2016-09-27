'''Sockets can be configured to act as a server and listen for incoming messages, or connect to other
applications as a client. After both ends of a TCP/IP socket are connected, communication is bi-directional.'''

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('', 8080)
print('starting up on {} port {}'.format(server_address[0], server_address[1]), file=sys.stderr)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection', file=sys.stderr)
    connection, client_address = sock.accept()

    try:
        # print >>sys.stderr, 'connection from', client_address
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            print('received "{}"'.format(data), file=sys.stderr)
            if data:
                print('sending data back to the client', file=sys.stderr)
                connection.sendall(b'Of couese!')
            else:
                print('no more data from {}'.format(client_address),  file=sys.stderr)
                break

    finally:
        # Clean up the connection
        connection.close()
