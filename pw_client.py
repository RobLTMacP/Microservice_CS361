# Author: Robert MacPherson
# GitHub username: RobLTMacP
# Date: 
# Description:
import json
import zmq
import time

FORMAT = 'utf-8'


def get_new_pw(pw_to_encrypt):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5050")

    socket.send_string(pw_to_encrypt)

    message = socket.recv()
    return message.decode(FORMAT)


def decode_old_pw(pw_to_decode):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5000")

    socket.send_string(pw_to_decode)

    message = socket.recv()
    return message.decode(FORMAT)

print('[PASSWORD REQUESTED] helloworld')
test_pw = get_new_pw('helloworld')
print(test_pw)
time.sleep(1)
print('NOW ATTEMPTING TO DECODE')
time.sleep(1)
print(decode_old_pw(test_pw))
