import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 1


def dumb_chat_server(port):
    """ A dumb chat server """
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM)
    # Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET,
                    socket.SO_REUSEADDR, 1)
    
    # Bind the socket to the port
    print(f"Starting up chat server on {host} port {port}")
    sock.bind((host, port))
    
    # Listen to clients, backlog argument specifies the max no.of queued connections
    sock.listen(backlog)

    print("Waiting a client")
    client, address = sock.accept()

    while True:
        print("Waiting a client's message")
        data = client.recv(data_payload)
        if data:
            print(f"client> {data.decode()}")

        message = input("> ")
        client.send(message.encode('utf-8'))
        
    # end connection
    client.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store",
                        dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    dumb_chat_server(port)
