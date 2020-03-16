import socket

host = "10.0.0.114"
porta = 6432

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('Digite a Mensagem: ')

    msg = msg.encode('utf-8')

    udp_socket.sendto(msg, (host, porta))
    udp_socket.recvfrom(512)

udp_socket.close()
