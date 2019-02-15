"""
Http to Modbus
Jonathan Coignard (Lawrence Berkeley National Laboratory)
jcoignard@lbl.gov
"""
from flask import Flask, request

app = Flask(__name__)
_version = '0.0.0'

@app.route('/write/<register>&<value>')
def write(register, value):
    return True

@app.route('/read/<register>')
def read(register):
    return True

@app.route('/ping')
def ping():
    return 'pinged :)'

if __name__ == '__main__':
    app.run(debug=True)
