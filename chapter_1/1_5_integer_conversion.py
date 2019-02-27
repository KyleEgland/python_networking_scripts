#! python3
# Python Network Programming Cookbook - Chapter 1
# This program originally written for Python 2.7 and re-written in Python 3
import socket


def convert_integer():
    data = 1234

    # 32-bit
    # ntohl() function converts from network byte order to host byte order in
    # long format - n=network, h=host, l=long
    long_byte = socket.ntohl(data)
    # htonl() function converts from host byte order to network byte order in
    # long format
    long_net_byte = socket.htonl(data)
    print(f'Original: {data} => Long host byte order: {long_byte}, Network \
byte order: {long_net_byte}')

    # 16-bit
    # ntohs() function converts from network byte order to host byte order in
    # short format - s=short
    short_byte = socket.ntohs(data)
    short_net_byte = socket.htons(data)
    print(f'Original: {data} => Short host byte order {short_byte}, Network \
byte order {short_net_byte}')


if __name__ == '__main__':
    convert_integer()
