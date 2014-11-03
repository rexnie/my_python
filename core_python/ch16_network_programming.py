#!/usr/bin/env python
import socket as skt
from time import ctime

BUFFER_SIZE = 1024

def run_tcp_server(host='', port=21567):
    server_addr = (host, port)
    tcp_server_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM) 
    tcp_server_socket.bind(server_addr)
    tcp_server_socket.listen(5)

    try:
        while True:
            print 'waiting for connetion...'
            tcp_client_socket, cli_addr = tcp_server_socket.accept()
            print '...conneted from:', cli_addr

            while True:
                data = tcp_client_socket.recv(BUFFER_SIZE)
                if not data:
                    break
                tcp_client_socket.send('(%s) %s' % (ctime(), data))
    except (KeyboardInterrupt, EOFError), err:
        print 'got error', err
        tcp_client_socket.close()
        tcp_server_socket.close()

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
    #run_tcp_server()
    #run_tcp_client(host='10.241.53.79') # server ip
    run_udp_server()
    #run_udp_client(host='10.241.53.79') # server ip
