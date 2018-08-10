#! python3
# Python Network Programming Cookbook - Chapter 1
# This program originally written for Python 2.7 and re-written for Python 3
# This program will create an NTP client which will get the current time from
# an NTP server
import ntplib
from time import ctime


def print_time():
    # Create an NTP client object
    ntp_client = ntplib.NTPClient()

    # Request the time
    response = ntp_client.request('pool.ntp.org')

    # Display time using the 'ctime' function to format the time
    print('[*] The time is {}'.format(ctime(response.tx_time)))


if __name__ == '__main__':
    print_time()
