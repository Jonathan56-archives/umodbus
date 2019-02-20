import socket
from umodbus import conf
from umodbus.client import tcp

# Enable values to be signed (default is False).
conf.SIGNED_VALUES = True
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '131.243.41.14'  # localhost
port = 502
sock.connect((ip_address, port))

# Data to test
data = [1, 2, 3, 4, 5]
print('Vector is ' + str(data))

# Returns a message or Application Data Unit (ADU) specific for doing
# Modbus TCP/IP.
message = tcp.write_multiple_registers(
    slave_id=1, starting_address=1, values=data)
response = tcp.send_message(message, sock)
print('Response from writing vector is ' + str(response))

message = tcp.read_input_registers(
    slave_id=1, starting_address=1, quantity=5)
response = tcp.send_message(message, sock)
print('Response from reading vector is '  + str(response))

sock.close()
