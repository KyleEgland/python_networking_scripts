#! python3
# Python Network Programming Cookbook - Chapter 1
# This program originally written fro Python 2.7 and re-written for Python 3
import socket


def test_socket_timeout():
    # Create socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Call the gettimeout() method in order to find out what the current
    # timeout is - defaults to None, which means timout is disabled
    print('Default socket timeout: {}'.format(s.gettimeout()))

    # Call the settimeout() method on the socket object and use an integer to
    # change from default
    s.settimeout(100)
    # Check the timeout again in order to show it has changed
    print('Current socket timeout: {}'.format(s.gettimeout()))


if __name__ == '__main__':
    test_socket_timeout()
