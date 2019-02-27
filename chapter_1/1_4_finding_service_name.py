#! python3
# Python Network Programming Cookbook - Chapter 1
# This program originally written for Python 2.7 and re-written in Python 3
import socket


def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25]:
        svc_name = socket.getservbyport(port, protocolname)
        print(f'Port:  {port} => service name:  {svc_name}')
    svc_name2 = socket.getservbyport(53, 'udp')
    print(f'Port:  53 => service name:  {svc_name2}')


if __name__ == '__main__':
    find_service_name()
