# Author: Robert MacPherson
# GitHub username: RobLTMacP
# Date: 
# Description:
import zmq
import passwordEncrypt

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5050")
FORMAT = 'utf-8'

print(['SERVER RUNNING ON PORT 5050...'])

while True:
    message = socket.recv()
    print(message.decode(FORMAT))
    operation = message.decode(FORMAT)
    print(operation)
    print(type(operation))
    print('[ENCRYPTION IN EFFECT...]')

    new_pw_req = operation
    new_encryption = passwordEncrypt.encrypt(new_pw_req)

    socket.send_string(new_encryption)
