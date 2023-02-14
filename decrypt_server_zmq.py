# Author: Robert MacPherson
# GitHub username: RobLTMacP
# Date: 
# Description:

import zmq
import passwordEncrypt

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5000")
FORMAT = 'utf-8'

print(['SERVER RUNNING ON PORT 5000...'])

while True:
    message = socket.recv()
    print(message.decode(FORMAT))
    operation = message.decode(FORMAT)
    print(operation)
    print(type(operation))

    print('[DECRYPTION IN EFFECT...]')

    decrypt_pw = operation
    return_to_client = passwordEncrypt.decrypt(decrypt_pw)

    socket.send_string(return_to_client)