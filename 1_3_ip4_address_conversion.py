#! python3
# Python Network Programming Cookbook - Chapter 1
# This program was originally written in Python 2.7 and re-written in Python 3
import socket
from binascii import hexlify


def convert_ip4_address(ip_list):
    for ip_addr in ip_list:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print('IP Address:  {} => Packed:  {}, Unpacked:  \
{}'.format(ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr))


if __name__ == '__main__':
    addr_str = input('[*] Enter IPs separated by commas (no spaces):  ')
    addr_lst = addr_str.split(',')
    print(f'You\'ve entered:  {addr_lst}')
    convert_ip4_address(addr_lst)
