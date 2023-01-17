from flask import Flask, request
import utils
import socket

app = Flask(__name__)

key_conf = None
switches = dict()
(conf, switches) = utils.configLoader()
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

@app.route('/ui')
def ui():
    global conf
    (conf, switches) = utils.configLoader()
    return utils.htmlGenerator(conf)

@app.route('/option', methods=['POST'])
def option():
    args = request.get_json()
    option = args.get('option')
    if option in conf:
        mode = conf.get(option).get('mode')
        key = conf.get(option).get('key')
        if mode == 'normal':
            if args.get('type')=='start':
                udp_sock.sendto(('start;'+str(key)).encode('utf-8'), ('127.0.0.1', 8080))
            else:
                udp_sock.sendto(('end;' + str(key)).encode('utf-8'), ('127.0.0.1', 8080))
        else:
            global switches
            if args.get('type')=='end':
                print(switches)
                if switches[option] == 0:
                    switches[option] = 1
                    udp_sock.sendto(('start;' + str(key)).encode('utf-8'), ('127.0.0.1', 8080))
                else:
                    switches[option] = 0
                    udp_sock.sendto(('end;' + str(key)).encode('utf-8'), ('127.0.0.1', 8080))


    return 'success'


if __name__=='__main__':
    app.run(host='0.0.0.0')