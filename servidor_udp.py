
import socket
HOST = '10.0.0.114'  # Definindo o IP do servidor
PORT = 6432  # Definindo a porta
port2 = 6433


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((HOST, PORT))
udp_socketResponse = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#udp_socketResponse.bind(HOST, )
print('Recebendo Mensagens...\n\n')
users = {}
while True:

    msg, cliente_ip = udp_socket.recvfrom(512)  # buffer de 512 bytes
    msg_decode = msg.decode('utf-8')
    if msg_decode == '!l':
        while True:
            print('Qual o login? ')
            msg, cliente_ip = udp_socket.recvfrom(512)
            msg_decode = msg.decode('utf-8')
            comando = msg_decode.split(' ')
            if comando[0] == '001':
                users.update({cliente_ip: comando[1]})
                udp_socketResponse.sendto(
                    b'Logado ', (cliente_ip[0], cliente_ip[1]))
                print('sucesso111')
                break

    print(cliente_ip, msg.decode('utf-8'))

udp_socket.close()
