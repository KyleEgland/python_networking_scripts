#! python
# Code from "Python Network Programming Cookbook", Second Edition, Chapter 7
import argparse
import xmlrpc
import threading
from xmlrpc.server import SimpleXMLRPCServer


# Trivial functions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - 7


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


class ServerThread(threading.Thread):
    def __init__(self, server_addr):
        threading.Thread.__init__(self)
        self.server = SimpleXMLRPCServer(server_addr)
        self.server.register_multicall_functions()
        self.server.register_function(add, 'add')
        self.server.register_function(subtract, 'subtract')
        self.server.register_function(multiply, 'multiply')
        self.server.register_function(divide, 'divide')

    def run(self):
        self.server.serve_forever()


def run_server(host, port):
    # Server code
    server_addr = (host, port)
    server = ServerThread(server_addr)
    server.start()
    print('Server thread started. Testing the server...')


def run_client(host, port):
    # Client code
    proxy = xmlrpc.client.ServerProxy("http://{}.{}/".format(host, port))

    multicall = xmlrpc.client.MultiCall(proxy)

    multicall.add(7, 3)
    multicall.subtract(7, 3)
    multicall.multipy(7, 3)
    multicall.divide(7, 3)
    result = multicall()
    print("7 + 3 = {},\n7 - 3 = {},\
          \n7 * 3 = {},\n7 / 3 = {}".format(tuple(result)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Multithreaded multicall '
                                     'XMLRPC Server/Proxy')
    parser.add_argument('--host', action='store', dest='host',
                        default='127.0.0.1')
    parser.add_argument('--port', action='store', dest='port', default=8000,
                        type=int)
    # Parse arguments
    given_args = parser.parse_args()
    host, port = given_args.host, given_args.port
    run_server(host, port)
    run_client(host, port)
