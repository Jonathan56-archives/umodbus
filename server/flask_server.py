"""
Http to Modbus
Jonathan Coignard (Lawrence Berkeley National Laboratory)
jcoignard@lbl.gov
"""
from flask import Flask, request, jsonify
import socket
from umodbus import conf
from umodbus.client import tcp

app = Flask(__name__)
_version = '0.0.0'
ip_address = '131.243.41.14'  # localhost
port = 502

@app.route('/write', methods=['POST'])
def write():
    # Connect to MODBUS master
    conf.SIGNED_VALUES = True
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip_address, port))

    c = request.get_json()
    for register, value in zip(c['registers'], c['values']):
        print(register)
        print(value)
        message = tcp.write_single_register(
            slave_id=1,
            address=int(register),
            value=int(value))
        _ = tcp.send_message(message, sock)

    # Close connection
    sock.close()
    return jsonify(payload=True)

@app.route('/read', methods=['POST'])
def read():
    # Connect to MODBUS master
    conf.SIGNED_VALUES = True
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip_address, port))

    c = request.get_json()
    responses = []
    for register in c['registers']:
        message = tcp.read_input_registers(
            slave_id=1, starting_address=register, quantity=1)
        responses.append(tcp.send_message(message, sock))

    # Close connection
    sock.close()
    return jsonify(payload=responses)

@app.route('/ping')
def ping():
    return 'pinged :)'

if __name__ == '__main__':
    # Run Flask and close the socket when Falk is killed
    app.run(debug=True)
