import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10002)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# Wait for a connection
print >>sys.stderr, 'Listening'

while True:
    connection, client_address = sock.accept()

    try:

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(50)
            if data:
                print >>sys.stderr, client_address, 'wrote: ', data
            else:
                break
            
    finally:
        # Clean up the connection
        connection.close()