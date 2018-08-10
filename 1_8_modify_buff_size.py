#! python3
# Python Network Programming Cookbook - Chapter 1
# This program originally written for Python 2.7 and re-written for Python 3
import socket


# Defining two constants to have the desired buffer size
SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096


def modify_buff_size():
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the current (default) size of the socket's send buffer
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print(f'Buffer size [Before]: {bufsize}')

    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    # This method takes three arguments:  level, optname, and value
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)

    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print(f'Buffer size [After]: {bufsize}')


if __name__ == '__main__':
    modify_buff_size()
