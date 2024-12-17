# http://www.py4e.com/code3.zip
import socket

# Create a socket object
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
mysocket.connect(('data.pr4e.org', 80))

# Prepare the GET request
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

# Send the GET request
mysocket.send(cmd)

# Receive and display the response
while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode())  # Decode and print the received data

# Close the socket
mysocket.close()

