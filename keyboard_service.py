from socket import *
import sys
import key_opt

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(('127.0.0.1', 8080))

while 1:
    try:
            data = udp_socket.recvfrom(1024)[0].decode('utf-8').split(';')
            type_ = data[0]
            key = int(data[1])

            print(data)

            if type_ == 'start':
                key_opt.key_down(key) #scancode 与 win32 不一致 https://www.win.tue.nl/~aeb/linux/kbd/scancodes-1.html
            else:
                key_opt.key_up(key)
    except KeyboardInterrupt:
        udp_socket.close()
        sys.exit()
