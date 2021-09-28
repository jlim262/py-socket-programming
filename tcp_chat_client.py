import socket
import sys
import argparse


host = 'localhost'
data_payload = 2048

def dumb_chat_client(port):
    """ A dumb chat client """
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect the socket to the server
    print(f"Connecting to {host} port {port}")
    sock.connect((host, port))
    # Send data
    try:
        while True:
            # Send data
            message = input("> ")
            if message == 'q':
                break
            sock.sendall(message.encode('utf-8'))
            # Look for the response
            data = sock.recv(data_payload)
            print(f"server> {data.decode()}")
    except socket.error as e:
        print(f"Socket error: {str(e)}")
    except Exception as e:
        print(f"Other exception: {str(e)}")
    finally:
        print("Closing connection to the server")
        sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store",
                        dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    dumb_chat_client(port)
