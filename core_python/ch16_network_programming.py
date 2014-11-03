#!/usr/bin/env python
import socket as skt
from time import ctime
import threading

BUFFER_SIZE = 1024

class MyThread(threading.Thread):
    """ tcp server threading main loop that communicate with client
        tcp_client_socket: the socket that return from accept method
        cli_addr: the address that return from accept method, a tuple
    """
    def __init__(self, tcp_client_socket, cli_addr):
        super(MyThread, self).__init__()
        self.tcp_client_socket = tcp_client_socket
        self.cli_addr = cli_addr
        self.loop = False
    def run(self):
        self.loop = True
        while self.loop:
            data = self.tcp_client_socket.recv(BUFFER_SIZE)
            if not data:
                break
            self.tcp_client_socket.send('(%s) %s' % (ctime(), data))

    def quit(self):
        self.loop = False

def run_tcp_server(host='', port=21567):
    server_addr = (host, port)
    tcp_server_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM) 
    tcp_server_socket.bind(server_addr)
    tcp_server_socket.listen(5)
    client_skt_addr_dict = {}
    print 'waiting for connection...'

    try:
        while True:
            tcp_client_socket, cli_addr = tcp_server_socket.accept()
            t = MyThread(tcp_client_socket, cli_addr)
            client_skt_addr_dict[(tcp_client_socket, cli_addr)] = t
            t.start()
            print '=' * 20
            for d in client_skt_addr_dict:
                print client_skt_addr_dict[d]

    except (KeyboardInterrupt, EOFError), err:
        print 'got error,cnt=', err, threading.active_count()
        for d in client_skt_addr_dict:
            t = client_skt_addr_dict[d]
            print 'cnt=', threading.active_count()
            t.quit()

        tcp_client_socket.close()
        tcp_server_socket.close()
        print client_skt_addr_dict, threading.active_count()

def run_tcp_client(host='localhost', port=21567):
    tcp_client_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
    tcp_client_socket.connect((host,port))

    try:
        while True:
            data = raw_input('> ')
            if not data:
                break
            tcp_client_socket.send(data)
            data = tcp_client_socket.recv(BUFFER_SIZE)
            if not data:
                break
            print data

    except (KeyboardInterrupt, EOFError), err:
        tcp_client_socket.close()

def run_udp_server(host='', port=21567):
    udp_server_socket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
    udp_server_socket.bind((host,port))

    try:
        while True:
            print 'waiting for message...'
            data, addr = udp_server_socket.recvfrom(BUFFER_SIZE)
            udp_server_socket.sendto('[%s] %s' % (ctime(), data), addr)
            print '...received and returned to:', addr

    except (KeyboardInterrupt, EOFError), err:
        udp_server_socket.close()

def run_udp_client(host='localhost', port=21567):
    udp_client_socket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)

    try:
        while True:
            data = raw_input('> ')
            if not data:
                break
            udp_client_socket.sendto(data, (host,port))
            data, addr = udp_client_socket.recvfrom(BUFFER_SIZE)
            if not data:
                break
            print data
    except (KeyboardInterrupt, EOFError), err:
        udp_client_socket.close()

if __name__ == '__main__':
    run_tcp_server()
    #run_tcp_client(host='10.241.53.79') # server ip
    #run_udp_server()
    #run_udp_client(host='10.241.53.79') # server ip
