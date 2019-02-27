#! python3
# Python Network Programming Cookbook - Chapter 1
# This program originally written for Python 2.7 and re-written for Python 3
# Normally, sockets cannot be re-used after closing.  This program will
# demonstrate how to re-use sockets
import socket


def reuse_socket_addr():
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the old state of the SO_REUSEADDR option
    old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print(f'[*] Old sock state: {old_state}')

    # Enable the SO_REUSEADDR option
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print(f'[*] New sock state: {new_state}')

    local_port = 8282
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(('127.0.0.1', local_port))
    srv.listen(1)
    print(f'[*] Listening on port: {local_port}')
    while True:
        try:
            connection, addr = srv.accept()
            print(f'[*] Connected by {addr[0]}:{addr[1]}')
        except KeyboardInterrupt:
            break
        except socket.error as msg:
            print(f'[-] msg')


if __name__ == '__main__':
    reuse_socket_addr()
