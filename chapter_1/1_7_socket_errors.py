#! python3
# Python Network Programming Cookbook - Chapter 1
# This program was originally written for Python 2.7 and adapted for Python 3
import sys
import socket
import argparse


def main():
    # Setup argumnet parsing
    parser = argparse.ArgumentParser(description='Socket Error Exampls')

    # Add arguments
    parser.add_argument('--host', action='store', dest='host', required=False)
    parser.add_argument('--port', action='store', dest='port', type=int,
                        required=False)
    parser.add_argument('--file', action='store', dest='file', required=False)

    given_args = parser.parse_args()

    host = given_args.host
    port = given_args.port
    filename = given_args.file

    # First try-except block - create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f'Error creating socket: {e}')
        sys.exit(1)

    # Second try-except block - connect to given host/port
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print(f'Address-related error connecting to server: {e}')
        sys.exit(1)
    except socket.error as e:
        print(f'Connection error: {e}')
        sys.exit(1)

    # Third try-except block - sending data
    try:
        file_obj = open(filename, 'r')
        text_obj = file_obj.read()
        file_obj.close()
        enc_payload = f'Get {text_obj} HTTP/1.0\r\n\r\n'.encode('utf-8')
        s.sendall(enc_payload)
    except socket.error as e:
        print(f'Error sending data: {e}')
        sys.exit(1)

    while 1:
        # Fourth try-except block - waiting to receive data from remote host
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print(f'Error receiving data: {e}')
            sys.exit(1)

        if not len(buf):
            break

        # Write received data
        sys.stdout.write(buf.decode('utf-8'))


if __name__ == '__main__':
    main()
