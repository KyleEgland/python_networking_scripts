#! ptyhon3
# Python Network Programming Cookbook - Chapter 1
# This program originally written for Python 2.7 and re-written for Python 3
# Changing a socket to blocking/non-blocking mode - default is blocking meaning
# that the socket will hold up the program until its work is done
import socket


def test_socket_modes():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Turn ON blocking
    s.setblocking(1)
    s.settimeout(0.5)
    # Bind socket object to address and port
    s.bind(('127.0.0.1', 0))

    socket_address = s.getsockname()
    print(f'Trivial Server launched on socket: {socket_address}')
    # This is simply an infinite loop to show that nothing can happen until the
    # socket's work is complete - which doesn't happen in this case
    while(1):
        s.listen(1)


if __name__ == '__main__':
    test_socket_modes()
