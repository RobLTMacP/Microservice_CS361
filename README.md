# Microservice_CS361

Description
This program is a simple server that listens on a specified port and waits for client requests. Upon receiving a request, it responds with a JSON file containing an encrypted password.

Prerequisites
Python 3.6 or higher
Usage
Clone this repository to your local machine.
Open a terminal and navigate to the project directory.
Run the following command to start the server:
Copy code
python server.py
The server will start listening on port 5000 by default. You can change the port by editing the PORT variable in server.py.
Use a client application (such as curl or a web browser) to send a GET request to the server. For example, to retrieve an encrypted password, run the following command:
bash
Copy code
curl http://localhost:5000/password
The server will respond with a JSON file containing the encrypted password.
Encryption
The key is randomly generated for each request, and is not stored on the server. 



![Sequence Diagram Client and Server Parallel Call Example](https://user-images.githubusercontent.com/61522594/218634573-b0711073-47c5-4761-b622-089dbf22f337.jpg)
