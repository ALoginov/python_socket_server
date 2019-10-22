import socket
import sys

# Connect the socket to the port where the server is listening
server_address = ('localhost', 11002)
print >>sys.stderr, 'connecting to %s port %s' % server_address

while True: 
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    
    print >>sys.stderr, 'Start messaging!'

    try:
        # get message
        message = raw_input()
        
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print >>sys.stderr, 'received: "%s"' % data

    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()