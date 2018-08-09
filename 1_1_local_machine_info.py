#! python3
# Python Network Programming Cookbook - Chapter 1
# This program was originally written for Python 2.6 and re-written in Python 3
import socket


def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print(f'Host name:  {host_name}')
    print(f'IP address:  {ip_address}')


if __name__ == '__main__':
    print_machine_info()
