#! python3
# Python Network Programming Cookbook - Chapter 1
# This program was originally written in Python 2.7 and re-written in Python 3
import socket


def get_remote_machine_info(machine):
    try:
        print('IP address:  {}'.format(socket.gethostbyname(machine)))
    except socket.error as err:
        print(f'{machine}:  {err}')


if __name__ == '__main__':
    remote_host = input('[*] Please enter machine address:  ')
    get_remote_machine_info(remote_host)
